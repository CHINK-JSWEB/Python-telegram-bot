# handlers/start.py
from telegram import Update
from telegram.ext import ContextTypes
import config
from keyboard.main_menu import main_menu_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if getattr(config, "ADMIN_ONLY_MODE", False) and user_id != getattr(config, "ADMIN_ID", None):
        await update.message.reply_text("🚫 The bot is currently *admin-only mode.*", parse_mode="Markdown")
        return

    await update.message.reply_text(
        "👋 Welcome Boss Jonnel! Pili ka ng option sa baba:",
        reply_markup=main_menu_keyboard()
    )
