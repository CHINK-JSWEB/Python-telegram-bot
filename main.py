# main.py

import threading
from flask import Flask
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
import config

from handlers.start import start
from handlers.help import help_command, help_fun, help_utils, help_admin
from handlers.callbacks import handle_callback
from handlers.welcome import welcome_new_member
from handlers.message_logger import log_message, show_history

# ------------ FLASK KEEP-ALIVE SERVER (Port 3000) -------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running on Render!"

def run_flask():
    app.run(host="0.0.0.0", port=3000)


# ------------ TELEGRAM BOT SETUP (POLLING MODE) ------------
def run_bot():
    # Gumamit ng direct token mula sa config.py
    application = Application.builder().token(config.BOT_TOKEN).build()

    # Commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("history", show_history))

    # Callback buttons
    application.add_handler(CallbackQueryHandler(handle_callback))

    # Welcome new members
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))

    # Log all messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, log_message))

    # Start polling
    print("🤖 Bot is running using POLLING...")
    application.run_polling()


# ------------ RUN BOTH SERVER + BOT ------------
if __name__ == "__main__":
    # Start Flask server in a separate thread
    threading.Thread(target=run_flask).start()
    # Start Telegram bot
    run_bot()
