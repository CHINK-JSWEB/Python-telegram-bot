from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if getattr(config, "ADMIN_ONLY_MODE", False) and user_id != getattr(config, "ADMIN_ID", None):
        await update.message.reply_text("🚫 The bot is currently *admin-only mode.*", parse_mode="Markdown")
        return

    keyboard = [
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🆘 Help", callback_data="help")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome Boss! Pili ka ng option sa baba:",
        reply_markup=reply_markup
    )
