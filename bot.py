import os
import threading
from flask import Flask
from telegram.ext import Updater, CommandHandler

# --- Flask setup (keeps Render happy with an open port) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    # Bind to port 10000 (Render expects a port)
    app.run(host="0.0.0.0", port=10000)

# --- Telegram bot setup ---
def run_bot():
    # Load token from environment variable
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set!")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # /start command
    def start(update, context):
        args = context.args
        if args:
            update.message.reply_text(f"Started with payload: {args[0]}")
        else:
            update.message.reply_text("Hello! Bot is alive.")

    # /ping command (silent health check)
    def ping(update, context):
        # Respond only to uptime services, not visible to normal users
        update.message.reply_text("pong")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))

    # Start polling Telegram
    print("✅ Bot started successfully and Flask is running")
    updater.start_polling()
    updater.idle()

# --- Run both Flask and Bot ---
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_bot()
