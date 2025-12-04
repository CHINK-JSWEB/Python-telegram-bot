from telegram import Update
from telegram.ext import ContextTypes
from handlers.start import start
from handlers.help import help_command, help_fun, help_utils, help_admin

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "about":
        await query.edit_message_text("ℹ️ This bot is made by Boss Jonnel.")
    elif data == "help":
        await help_command(update, context)
    elif data == "contact":
        await query.edit_message_text("📞 Contact Boss Jonnel for inquiries.")
    elif data == "back_to_main":
        await start(update, context)
    elif data == "help_main":
        await help_command(update, context)

    # Fun
    elif data == "help_fun":
        await help_fun(update, context)
    elif data == "help_utils":
        await help_utils(update, context)
    elif data == "help_admin":
        await help_admin(update, context)
