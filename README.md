# DirWatch Telegram Alert

A tiny command‑line tool that watches a folder and sends a Telegram message whenever a file is created, modified, or deleted. Great for quick monitoring and instant build alerts.

## Installation

```bash
pip install watchdog python-telegram-bot
```

## Usage

```bash
python dirwatch.py /path/to/watch YOUR_TELEGRAM_BOT_TOKEN YOUR_CHAT_ID
```

- **/path/to/watch** – directory to monitor
- **YOUR_TELEGRAM_BOT_TOKEN** – token from @BotFather
- **YOUR_CHAT_ID** – numeric chat ID (use @userinfobot to get it)

## How it works

The script uses `watchdog` to listen for filesystem events and `python-telegram-bot` to post a message to the specified chat.

## License

MIT
