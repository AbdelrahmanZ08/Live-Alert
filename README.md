# $Live Transaction Alert Bot

## How It Works

1. **Telegram Integration**:
   - The bot does **not** use the Helius API to get transaction data. Instead, it listens to a [private Telegram group](https://t.me/Livepricealerts) where a Safeguard bot is providing transaction alerts.
   - The Telegram Safeguard bot sends messages to the group with transaction details such as the transaction amount.

2. **Transaction Matching**:
   - The bot checks if the transaction amount is above the threshold specified in the script (e.g., $4900 (20SOL).
   - If the transaction amount matches or exceeds the threshold, the bot triggers an audio alert.

3. **Discord Integration**:
   - The bot connects to a Discord voice channel (defined by the `DISCORD_CHANNEL_ID`).
   - It uses the **FFmpeg** library to play an MP3 audio file in the voice channel.
   - The bot remains connected to the voice channel and will play the alert whenever a qualifying transaction is detected.

## Requirements

- **Discord.py** (For interacting with Discord)
- **Telethon** (For interacting with Telegram)
- **FFmpeg** (For playing audio in the Discord voice channel)

You can install the requirements.txt using `pip`:

```bash
pip install -r requirements.txt

```

[Testing server](https://discord.gg/jd8zRAnTEE)
[Alert VC](https://discord.gg/ZPF2Ay56)
[Transactions Chat](https://discord.gg/zBQRaJE9)
[repo](https://github.com/AbdelrahmanZ08/Live-Alerta)
