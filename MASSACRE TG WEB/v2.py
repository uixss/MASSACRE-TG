import requests
import random
import json
import os
import threading
from queue import Queue


USERS_FILENAME = "main.json"
LOG_FILENAME = "results.log"

COLORS = {"rd": "\033[91m", "cn": "\033[0m", "yw": "\033[93m"}

def generate_user_agents():
    user_agents = []
    bases = [
        "Mozilla/5.0 ({system}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version} Safari/537.36",
        "Mozilla/5.0 ({system}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Mobile/15E148 Safari/604.1",
    ]
    systems = [
        "Windows NT 10.0; Win64; x64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "Linux; Android 8.0.0; Plume L2",
        "iPhone; CPU iPhone OS 16_0 like Mac OS X",
    ]
    browsers = [
        ("Chrome", [99, 100, 110, 116]),
        ("Safari", [12, 13, 14, 15]),
        ("Opera", [50, 60, 70, 80]),
        ("Brave", [1, 1.2, 1.3, 1.5]),
        ("Mozilla", [50, 60, 70, 100]),
    ]

    for _ in range(100):
        system = random.choice(systems)
        browser, versions = random.choice(browsers)
        version = random.choice(versions)
        base = random.choice(bases)
        user_agents.append(base.format(system=system, browser=browser, version=version))

    return user_agents
def generate_phone_number(prefix="+54", length=10):
    digits = "0123456789"
    random_digits = "".join(random.choice(digits) for _ in range(length))
    return f"{prefix}{random_digits}"

def read_emails(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]
    
def read_messages(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data.get("SPAM", [])

def load_users():
    if not os.path.exists(USERS_FILENAME):
        print(f"{COLORS['rd']}Error: Archivo de usuarios no encontrado.{COLORS['cn']}")
        return []

    try:
        with open(USERS_FILENAME, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            users = []
            for entry in raw_data:
                try:
                    if entry.get("status") == "success":
                        info = entry["info"]
                        user_id = info["id"]
                        user_link = info.get("user") or info.get("username") or "N/A"

                        users.append({"id": user_id, "link": user_link})
                except KeyError as e:
                    print(f"{COLORS['yw']}Advertencia: Clave faltante en entrada {entry}: {e}{COLORS['cn']}")
            return users
    except Exception as e:
        print(f"{COLORS['rd']}Error al cargar usuarios: {str(e)}{COLORS['cn']}")
        return []

def log_result(status, email, message, response_code, user):
    with open(LOG_FILENAME, "a") as log_file:
        log_file.write(
            f"{status} | Email: {email} | User: {user['link']} (ID: {user['id']}) | "
            f"Message: {message[:50]}... | Response Code: {response_code}\n"
        )

def process_email(email, messages, users, user_agents):
    session = requests.Session()

    user_agent = random.choice(user_agents)
    message = random.choice(messages)
    user = random.choice(users)  # Seleccionar un usuario al azar
    user_info = f"\nLinked User: {user['link']} (ID: {user['id']})"
    final_message = message + user_info

    headers_get = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Connection": "keep-alive",
    }

    try:
        response_get = session.get("https://telegram.org/support", headers=headers_get)
        if response_get.status_code == 200:
            print(f"[+] GET exitoso para {email}.")
        else:
            print(f"[-] GET fallido para {email}. Código: {response_get.status_code}")
            log_result("GET Failed", email, final_message, response_get.status_code, user)
            return
        phone = generate_phone_number()
        data_post = {
            "message": final_message,
            "email": email,
            "phone": phone,
            "setln": "es"
        }

        headers_post = {
            "Host": "telegram.org",
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://telegram.org",
            "Connection": "keep-alive",
            "Referer": "https://telegram.org/support",
        }

        response_post = session.post("https://telegram.org/support", headers=headers_post, data=data_post)
        if response_post.status_code == 200:
            print(f"[+] POST exitoso para {email}.")
            log_result("POST Success", email, final_message, response_post.status_code, user)
        else:
            print(f"[-] POST fallido para {email}. Código: {response_post.status_code}")
            log_result("POST Failed", email, final_message, response_post.status_code, user)
    except Exception as e:
        print(f"[-] Error procesando {email}: {str(e)}")
        log_result("Exception", email, final_message, str(e), user)


def main():
    user_agents = generate_user_agents()
    emails = read_emails("emails.txt")
    messages = read_messages("report.json")
    users = load_users()

    if not emails or not messages or not users:
        print("[-] Faltan datos para procesar solicitudes.")
        return

    queue = Queue()
    threads = []

    for email in emails:
        queue.put(email)
        
    def worker():
        while not queue.empty():
            email = queue.get()
            process_email(email, messages, users, user_agents)
            queue.task_done()

    for _ in range(5): 
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
