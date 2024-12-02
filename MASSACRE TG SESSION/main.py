import os
import platform
import random
import asyncio
import pickle
from telethon import TelegramClient, types, functions, errors
import json
from telethon.sync import TelegramClient
from telethon.errors import (
    PhoneNumberBannedError,
    SessionPasswordNeededError,
    RPCError
)
from tabulate import tabulate

SESSIONS_FILENAME = 'vars.txt'
CONFIG_FILENAME = 'report.json'
USERS_FILENAME = 'main.json'
COLORS = {
    'gn': '\033[92m', 
    'rd': '\033[91m', 
    'yw': '\033[93m',  
    'cn': '\033[0m'   
}

def load_sessions():
    if not os.path.exists(SESSIONS_FILENAME):
        print(f"{COLORS['rd']}Error: Archivo de sesiones no encontrado.{COLORS['cn']}")
        return []

    sessions = []
    try:
        with open(SESSIONS_FILENAME, 'rb') as f:
            while True:
                try:
                    sessions.append(pickle.load(f))
                except EOFError:
                    break
    except Exception as e:
        print(f"{COLORS['rd']}Error al cargar sesiones: {str(e)}{COLORS['cn']}")
    return sessions

def check_sessions():
    sessions = load_sessions()
    valid_sessions = []

    for api_id, api_hash, phone in sessions:
        client = TelegramClient(f'sessions/{phone}', api_id, api_hash)
        try:
            client.connect()
            if not client.is_user_authorized():
                print(f"{COLORS['yw']}[!] {phone} necesita inicio de sesión.{COLORS['cn']}")
                continue

            print(f"{COLORS['gn']}[+] Sesión válida: {phone}{COLORS['cn']}")
            valid_sessions.append((api_id, api_hash, phone))
        except PhoneNumberBannedError:
            print(f"{COLORS['rd']}[!] {phone} está baneado y será omitido.{COLORS['cn']}")
        except SessionPasswordNeededError:
            print(f"{COLORS['yw']}[!] {phone} requiere autenticación 2FA y será omitido.{COLORS['cn']}")
        except RPCError as e:
            print(f"{COLORS['rd']}[!] Error con {phone}: {e}{COLORS['cn']}")
        except Exception as e:
            print(f"{COLORS['rd']}[!] Error desconocido con {phone}: {e}{COLORS['cn']}")
        finally:
            client.disconnect()

    print(f"{COLORS['gn']}[+] Sesiones válidas {len(valid_sessions)}{COLORS['cn']}")
    return valid_sessions

def load_config():
    if not os.path.exists(CONFIG_FILENAME):
        print(f"{COLORS['rd']}Error: Archivo de configuración no encontrado.{COLORS['cn']}")
        return {}
    with open(CONFIG_FILENAME, 'r') as f:
        return json.load(f)

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
                        user_link = info.get("user", "N/A")
                        users.append({"id": user_id, "link": user_link})
                except KeyError as e:
                    print(f"{COLORS['yw']}Advertencia: Clave faltante en entrada {entry}: {e}{COLORS['cn']}")
            return users
    except Exception as e:
        print(f"{COLORS['rd']}Error al cargar usuarios: {str(e)}{COLORS['cn']}")
        return []

class TelegramReporter:
    def __init__(self, sessions, config, users):
        self.sessions = sessions
        self.config = config
        self.users = users
        self.session_index = 0

        self.methods = {
            "SPAM": types.InputReportReasonSpam(),
            "COPYRIGHT": types.InputReportReasonCopyright(),
            "FAKE": types.InputReportReasonFake(),
            "PERSONAL_DETAILS": types.InputReportReasonPersonalDetails()
        }

    def get_next_session(self):
        if not self.sessions:
            print(f"{COLORS['rd']}No hay sesiones disponibles.{COLORS['cn']}")
            return None

        session = self.sessions[self.session_index]
        self.session_index = (self.session_index + 1) % len(self.sessions)
        return session

    def get_random_message(self, report_type=None):
        if "SPAM" in self.config and self.config["SPAM"]:
            return random.choice(self.config["SPAM"])
        else:
            print(f"{COLORS['rd']}Advertencia: No se encontraron mensajes de reporte en la configuración.{COLORS['cn']}")
            return "Reporte generado automáticamente."


    async def report_channel_messages(self, client, entity, report_type):
        try:
            messages = await client.get_messages(entity, limit=10)
            for message in messages:
                msg_id = message.id
                report_message = self.get_random_message(report_type)
                await client(functions.messages.ReportRequest(
                    peer=entity,
                    id=[msg_id],
                    reason=self.methods[report_type],
                    message=report_message
                ))
                print(f"{COLORS['gn']}Mensaje {msg_id} reportado en el canal.{COLORS['cn']}")
                await asyncio.sleep(2)
        except Exception as e:
            print(f"{COLORS['rd']}Error al reportar mensajes del canal: {str(e)}{COLORS['cn']}")

    async def report_users(self):
        report_table = []

        for session in self.sessions:
            api_id, api_hash, phone = session
            print(f"{COLORS['yw']}Iniciando reportes con la sesión {phone}{COLORS['cn']}")

            async with TelegramClient(f'sessions/{phone}', api_id, api_hash) as client:
                if not await client.is_user_authorized():
                    print(f"{COLORS['rd']}Sesión no autorizada: {phone}{COLORS['cn']}")
                    continue

                for user in self.users:
                    user_id = user["id"]
                    user_link = user["link"]
                    print(f"{COLORS['gn']}Reportando {user_id} ({user_link}) usando la sesión {phone}{COLORS['cn']}")

                    for report_type in self.methods.keys():
                        try:
                            # Obtener entidad y mostrar información
                            entity = await client.get_entity(user_link)
                            if isinstance(entity, types.User):
                                print(f"{COLORS['gn']}Entidad: Usuario\n• Nombre: {entity.first_name or ''} {entity.last_name or ''}\n• ID: {entity.id}{COLORS['cn']}")
                                report_message = self.get_random_message(report_type)
                                await client(functions.account.ReportPeerRequest(
                                    peer=entity,
                                    reason=self.methods[report_type],
                                    message=report_message
                                ))
                                print(f"{COLORS['gn']}Usuario {user_id} reportado.{COLORS['cn']}")
                            elif isinstance(entity, (types.Channel, types.Chat)):
                                print(f"{COLORS['yw']}Reportando mensajes del canal o grupo: {user_link}{COLORS['cn']}")
                                await self.report_channel_messages(client, entity, report_type)
                            
                            report_table.append([phone, user_link, report_type])
                        except Exception as e:
                            print(f"{COLORS['rd']}Error al reportar {user_link}: {str(e)}{COLORS['cn']}")
                        await asyncio.sleep(2)  # Delay entre reportes para evitar límites de Telegram

        # Mostrar resultados de los reportes
        if report_table:
            print(f"\n{COLORS['yw']}Resultados de los reportes:{COLORS['cn']}")
            print(tabulate(report_table, headers=["Sesión", "Usuario/Canal", "Reporte"], tablefmt="grid"))
        else:
            print(f"{COLORS['rd']}No se enviaron reportes válidos.{COLORS['cn']}")


if __name__ == "__main__":
    if 'Windows' in platform.system():
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    sessions = check_sessions()
    config = load_config()
    users = load_users()

    if sessions and config and users:
        reporter = TelegramReporter(sessions, config, users)
        asyncio.run(reporter.report_users())
    else:
        print(f"{COLORS['rd']}Faltan sesiones, configuración o usuarios para iniciar.{COLORS['cn']}")