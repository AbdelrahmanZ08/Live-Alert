import discord
from discord.ext import commands
from telethon import TelegramClient, events
import re
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
THRESHOLD_AMOUNT = float(os.getenv('THRESHOLD_AMOUNT'))
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))
MP3_FILE_PATH = os.getenv('MP3_FILE_PATH')
FFMPEG_PATH = os.getenv('FFMPEG_PATH')
TELEGRAM_CHAT = os.getenv('TELEGRAM_GROUP_USERNAME')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

voice_client = None

@bot.event
async def on_ready():
    print(f'Discord Bot logged in as {bot.user}')
    await start_telegram_client()
    await connect_to_voice_channel()

async def connect_to_voice_channel():
    global voice_client
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    
    if channel:
        try:
            voice_client = await channel.connect()
        except Exception as e:
            print(f"Error connecting to voice channel: {e}")

async def start_telegram_client():
    client = TelegramClient('session_name', api_id, api_hash)
     
    @client.on(events.NewMessage(chats=TELEGRAM_CHAT))
    async def handler(event):
        message = event.raw_text
        amount_match = re.search(r'💵 \$([\d,.]+)', message)
         
        if amount_match:
            amount = float(amount_match.group(1).replace(',', ''))
             
            if amount >= THRESHOLD_AMOUNT:
                print(f"🚨 Alert! Transaction value is ${amount}")
                await play_alert_sound()
                await send_transaction_notification(amount, message)

    await client.start()
    print("Telegram monitoring started...")

async def play_alert_sound():
    global voice_client
    
    if voice_client and not voice_client.is_playing():
        try:
            voice_client.play(discord.FFmpegPCMAudio(MP3_FILE_PATH, executable=FFMPEG_PATH))
        except Exception as e:
            print(f"Error playing sound: {e}")

async def send_transaction_notification(amount, original_message):
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        notification_message = f"🚨 High-Value Transaction Detected! 💰\n" \
                                f"Amount: ${amount:,.2f}\n" \
                                f"Original Message: {original_message}"
        await channel.send(notification_message)

bot.run(DISCORD_BOT_TOKEN)
