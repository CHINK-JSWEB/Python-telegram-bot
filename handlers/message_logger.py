from telegram import Update
from telegram.ext import ContextTypes

MAX_LOGS = 10

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    chat_id = update.effective_chat.id
    text = update.message.text or "<Non-text message>"
    user = update.effective_user.full_name

    logs = context.chat_data.get("message_logs", [])
    logs.append(f"{user}: {text}")
    if len(logs) > MAX_LOGS:
        logs = logs[-MAX_LOGS:]

    context.chat_data["message_logs"] = logs

async def show_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logs = context.chat_data.get("message_logs", [])
    if not logs:
        await update.message.reply_text("📭 Wala pang na-log na message.")
        return
    history_text = "\n".join(logs)
    await update.message.reply_text(f"🕓 Last {len(logs)} Messages:\n\n{history_text}")
