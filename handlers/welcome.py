# handlers/welcome.py
from telegram import Update
from telegram.ext import ContextTypes

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"🎉 Welcome {member.mention_html()} sa group, enjoy your stay!",
            parse_mode="HTML"
        )
