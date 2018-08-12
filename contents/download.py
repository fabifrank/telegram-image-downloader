from telethon import TelegramClient, sync
import sys
import logging

api_id = sys.argv[1]
api_hash = sys.argv[2]
phone = sys.argv[3]
download_folder = sys.argv[4]
chats = sys.argv[5]

chats = chats.split(',')

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)

dialogs = client.get_dialogs()

for chat in chats:
    msgs = client.get_messages(chat)
    for msg in msgs:
        msg.download_media(file=download_folder)