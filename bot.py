import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Load token from environment variable
TOKEN = os.environ["TOKEN"]

# Hidden group link behind JOIN button
JOIN_URL = "https://t.me/+PtEYqHB3wYljMjQ1"

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("JOIN", url=JOIN_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Click below:", reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()