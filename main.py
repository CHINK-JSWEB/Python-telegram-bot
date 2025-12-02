import nest_asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from config import TOKEN
from handlers.start import start
from handlers.help import help_command
from handlers.callbacks import handle_callback
from handlers.message_logger import log_message, show_history

nest_asyncio.apply()

def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("history", show_history))  # 🆕 show history command

    # Inline callbacks
    app.add_handler(CallbackQueryHandler(handle_callback))

    # 🆕 Message logger (lahat ng text messages)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, log_message))

    print("🤖 Bot is running boss...")
    app.run_polling()

if __name__ == "__main__":
    main()
