# Discord Telegram Transaction Alert Bot

This bot listens to transaction alerts from a **private Telegram group** and plays an audio alert when the transaction amount exceeds a set threshold. The bot is connected to a **Discord voice channel** and plays a sound when a qualifying transaction occurs.

## Features

- **Transaction Monitoring**: The bot monitors a private Telegram group using the Telegram Safeguard bot for transaction alerts.
- **Audio Alerts**: When a transaction exceeds the defined threshold, the bot will play an audio alert in a connected Discord voice channel.
- **Always Connected to Voice Chat**: The bot is designed to stay connected to the voice channel and automatically play the audio alert when a transaction is detected.

## How It Works

1. **Telegram Integration**:
   - The bot does **not** use the Helius API to get transaction data. Instead, it listens to a private Telegram group where a Safeguard bot is providing transaction alerts.
   - The Telegram Safeguard bot sends messages to the group with transaction details such as the transaction amount.

2. **Transaction Matching**:
   - The bot checks if the transaction amount is above the threshold specified in the script (e.g., $4900).
   - If the transaction amount matches or exceeds the threshold, the bot triggers an audio alert.

3. **Discord Integration**:
   - The bot connects to a Discord voice channel (defined by the `DISCORD_CHANNEL_ID`).
   - It uses the **FFmpeg** library to play an MP3 audio file in the voice channel.
   - The bot remains connected to the voice channel and will play the alert whenever a qualifying transaction is detected.

## Requirements

- **Python 3.7+**
- **Discord.py** (For interacting with Discord)
- **Telethon** (For interacting with Telegram)
- **FFmpeg** (For playing audio in the Discord voice channel)

You can install the required dependencies using `pip`:

```bash
pip install discord.py telethon python-dotenv
