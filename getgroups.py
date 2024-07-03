from telethon import TelegramClient, sync

# Replace these with your own values
api_id = '27557492'
api_hash = '1fc2002a5ed60a0e5a1f93cb0e411ff8'
phone_number = '+972503962170'

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone_number)
    
    # Get dialogs (chats)
    dialogs = await client.get_dialogs()

    # Print group IDs and names
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            print(f"Name: {dialog.name}, ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
