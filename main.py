import os
import threading
from time import sleep
import pyrogram
from pyrogram import Client, filters

bot_token = os.environ.get("TOKEN", "")
api_hash = os.environ.get("HASH", "")
api_id = os.environ.get("ID")
auth_chat = os.environ.get("AUTH_CHANNEL", [-1001602634418])
del_users_id = os.environ.get("DEL_USERS_ID", [1458192575, 5293418498])

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def delthread(message):
    if message.from_user.id in del_users_id:
        sleep(600)
        try:
            app.delete_messages(message.chat.id, message.id)
        except:
            print(f"Can't Delete Message {message.id}")
            return
    else:
        return

@app.on_message(filters.chat(auth_chat))
def receive(
    client: pyrogram.client.Client,
    message: pyrogram.types.messages_and_media.message.Message,
):
    delmsg = threading.Thread(target=lambda: delthread(message), daemon=True)
    delmsg.start()

# server loop
print("Bot Starting")
app.run()
