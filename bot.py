import random
import asyncio
from telethon import TelegramClient, events, errors
from datetime import datetime, time

# Replace these with your own values
api_id = '27557492'
api_hash = '1fc2002a5ed60a0e5a1f93cb0e411ff8'
phone_number = '+972503962170'

# List of group IDs or names
group_ids = [-1001534750171, -1001444468254, -1001516227057, -1001857353345, -1001808712511, -1001328372400, -1001301606845, -1001246503749, -1001392772096, -1001692212602, -1001394527357, -1001361929514, -1001258862444, -1001407141865]

# Array of messages to be chosen randomly
messages = [
    "היי",
    "משעמם",
    "מרכז?",
    "חם היוםם",
    "יש פה אנשים בכלל?"
]

# Predefined response message for private messages
predefined_message = "דבר איתי פה: https://t.me/PassionVideoBot"

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

def get_interval():
    now = datetime.now().time()
    if time(22, 0) <= now or now < time(5, 0):
        return 45 * 60  # 45 minutes in seconds
    else:
        return 90 * 60  # 1.5 hours in seconds

async def send_messages():
    while True:
        if not client.is_connected():
            await client.connect()
        for group_id in group_ids:
            message = random.choice(messages)
            try:
                await client.send_message(group_id, message)
                print(f"Sent message to group {group_id}: {message}")
            except errors.FloodWaitError as e:
                print(f"Sleeping for {e.seconds} seconds due to flood wait")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"Failed to send message to group {group_id}: {e}")
        interval = get_interval()
        await asyncio.sleep(interval)

@client.on(events.NewMessage(incoming=True))
async def handle_new_message(event):
    if event.is_private:  # Only respond to private messages
        await event.respond(predefined_message)
        print(f"Responded to {event.sender_id}")

async def main():
    await client.start(phone_number)
    await client.run_until_disconnected()

# Run the periodic message sending in the background
client.loop.create_task(send_messages())

# Run the main function to start the client and listen for events
with client:
    client.loop.run_until_complete(main())