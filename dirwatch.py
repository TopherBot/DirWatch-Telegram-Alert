import sys
import argparse
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from telegram import Bot

class TelegramHandler(FileSystemEventHandler):
    def __init__(self, bot: Bot, chat_id: int):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id

    def _send(self, action: str, src_path: str):
        filename = Path(src_path).name
        message = f"🛎 *{action}* – `{filename}`"
        self.bot.send_message(chat_id=self.chat_id, text=message, parse_mode='Markdown')

    def on_created(self, event):
        if not event.is_directory:
            self._send('Created', event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self._send('Modified', event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self._send('Deleted', event.src_path)

def main():
    parser = argparse.ArgumentParser(description='Watch a directory and send Telegram alerts on changes.')
    parser.add_argument('path', help='Directory to watch')
    parser.add_argument('token', help='Telegram bot token')
    parser.add_argument('chat_id', type=int, help='Telegram chat ID to receive alerts')
    args = parser.parse_args()

    watch_path = Path(args.path).resolve()
    if not watch_path.is_dir():
        print(f"Error: {watch_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    bot = Bot(token=args.token)
    event_handler = TelegramHandler(bot, args.chat_id)
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=True)
    observer.start()
    print(f"🚀 Watching {watch_path} – alerts will be sent to chat {args.chat_id}")
    try:
        while True:
            pass  # keep the script running; Ctrl+C to stop
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
