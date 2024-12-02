import asyncio
import os
import json
from telethon import TelegramClient, functions, types, errors
from telethon.sessions import StringSession

async def load_or_create_session():
    session_file = 'user_session.session'

    if os.path.exists(session_file):
        try:
            with open(session_file, 'rb') as f:
                session_string = f.read().decode('utf-8').strip()
                return StringSession(session_string)
        except (UnicodeDecodeError, ValueError) as e:
            print(f"Error al cargar el archivo de sesión: {e}. Creando una nueva sesión...")
            os.remove(session_file)
            return await create_new_session(session_file)
    else:
        print("No se encontró la sesión. Creando una nueva sesión...")
        return await create_new_session(session_file)

async def create_new_session(session_file):
    api_id = ''  
    api_hash = '' 
    phone = '+'  

    client = TelegramClient(StringSession(), api_id, api_hash)

    async with client:
        await client.start(phone)
        session_string = client.session.save()
        with open(session_file, 'wb') as f:
            f.write(session_string.encode('utf-8'))
        print(f"Sesión creada y guardada en '{session_file}'")
        return StringSession(session_string)

def load_user_data():
    try:
        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as f:
                return [line.strip() for line in f if line.strip()]
        else:
            print("El archivo 'users.txt' no existe.")
            return []
    except Exception as e:
        print(f"Error al cargar el archivo 'users.txt': {e}")
        return []

async def process_entity(client, entity_input, admin_limit=100):
    if not entity_input:
        return {"status": "invalid_input", "details": "Empty or None input", "link": "N/A", "input": entity_input}

    try:
        entity = await client.get_entity(entity_input)
        link = f"https://t.me/{entity.username}" if hasattr(entity, 'username') and entity.username else "N/A"

        if isinstance(entity, types.User):
            return {
                "status": "success",
                "input": entity_input,
                "type": "user",
                "link": link,
                "info": {
                    "id": entity.id,
                    "user": entity_input,  
                    "username": entity.first_name or "N/A",
                    "name": f"{entity.first_name or ''} {entity.last_name or ''}".strip(),
                    "is_bot": "Yes" if entity.bot else "No",
                },
            }

        elif isinstance(entity, types.Channel):
            full_chat = await client(functions.channels.GetFullChannelRequest(entity))
            chat_type = "public" if entity.username else "private"
            metadata = {
                "id": entity.id,
                "title": entity.title,
                "username": f"@{entity.username or 'N/A'}",
                "members": full_chat.full_chat.participants_count,
                "description": full_chat.full_chat.about or "N/A",
                "admins": [],
            }

            try:
                offset, total_admins = 0, []
                while True:
                    admins_data = await client(functions.channels.GetParticipantsRequest(
                        channel=entity,
                        filter=types.ChannelParticipantsAdmins(),
                        offset=offset,
                        limit=admin_limit,
                        hash=0,
                    ))
                    total_admins.extend([
                        {
                            "id": admin.user_id,
                            "username": admin.user.first_name or "N/A",  
                            "user": f"@{admin.user.username or 'N/A'}", 
                            "arorab": admin.rank if hasattr(admin, 'rank') else "N/A",
                            "link": f"https://t.me/{admin.user.username}" if admin.user.username else "N/A",
                        }
                        for admin in admins_data.participants if isinstance(admin, types.ChannelParticipantAdmin)
                    ])
                    if len(admins_data.participants) < admin_limit:
                        break
                    offset += admin_limit

                metadata["admins"] = total_admins
            except errors.ChatAdminRequiredError:
                metadata["admins"] = "Restricted (Admin privileges required)"
            except Exception as e:
                metadata["admins"] = f"Error retrieving admins: {str(e)}"

            return {
                "status": "success",
                "input": entity_input,
                "type": "channel" if not entity.megagroup else "group",
                "privacy": chat_type,
                "link": link,
                "info": metadata,
            }
        else:
            return {"status": "unknown_entity", "input": entity_input, "link": link, "details": "Entity type not recognized"}

    except (errors.UserDeactivatedError, errors.AuthKeyInvalidError) as e:
        return {"status": "account_issue", "details": str(e), "link": "N/A", "input": entity_input}
    except errors.ChannelPrivateError:
        return {"status": "private_channel", "link": "N/A", "details": "Channel is private or access is denied", "input": entity_input}
    except errors.FloodWaitError as e:
        print(f"FloodWaitError: Esperando {e.seconds} segundos...")
        await asyncio.sleep(e.seconds)
        return {"status": "flood_wait", "link": "N/A", "details": f"Flood wait for {e.seconds} seconds", "input": entity_input}
    except errors.RPCError as e:
        return {"status": "rpc_error", "link": "N/A", "details": str(e), "input": entity_input}
    except Exception as e:
        return {"status": "error", "link": "N/A", "details": str(e), "input": entity_input}
async def main():
    session = await load_or_create_session()
    user_data = load_user_data()

    if not session:
        print("No se encontró una sesión válida.")
        return
    if not user_data:
        print("No se encontraron datos de usuarios para verificar.")
        return

    api_id = ''  
    api_hash = ''  

    client = TelegramClient(session, api_id, api_hash)
    valid_data = []  
    async with client:
        for entity_input in user_data:
            print(f"Procesando: {entity_input}")
            data = await process_entity(client, entity_input)
            valid_data.append(data)  
            print(f"{entity_input}: {data}")

    with open('valid_data.json', 'w', encoding='utf-8') as f:
        json.dump(valid_data, f, ensure_ascii=False, indent=4)
    print(f"Datos válidos guardados en 'valid_data.json'.")

if __name__ == "__main__":
    asyncio.run(main())
