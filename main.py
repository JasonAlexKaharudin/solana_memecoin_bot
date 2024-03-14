#####################################################################
from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME')
GROUP_USERNAME = os.getenv('GROUP_USERNAME')

bot_client = TelegramClient('bot-sesh', API_ID, API_HASH).start(bot_token=BOT_API_TOKEN)
client = TelegramClient('fella', API_ID, API_HASH).start()

@client.on(events.NewMessage(chats=CHANNEL_USERNAME, outgoing=False))
async def my_event_handler(event):
    print("GOT NEW EVENT")
    group_entity = await bot_client.get_entity(GROUP_USERNAME)
    message = str(event.message)
    # Security checks
    security_fields = ["Mutable Metadata: Yes", "Mint Authority: Yes", "Freeze Authority: Yes", "LP Burned: Yes"]
    score = 0
    for field in security_fields:
        if field in message:
            score += 1
    # Conditions
    if ("Score: Good" in message or "Score: Neutral" in message) and score >= 3:
        # Send to fuckers
        await bot_client.send_message(group_entity, event.message)
        print("Messages BroadCasted :)")
    else:
        print("Get Rugged Larh")

client.run_until_disconnected()