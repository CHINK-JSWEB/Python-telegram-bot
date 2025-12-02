from telegram import Update
from telegram.ext import ContextTypes

MAX_LOGS = 10  # limit ng history

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """I-save lahat ng messages sa chat_data (last 10 only)."""
    if not update.message:
        return

    chat_id = update.effective_chat.id
    text = update.message.text or "<Non-text message>"
    user = update.effective_user.full_name

    # Kunin logs per group/chat
    logs = context.chat_data.get("message_logs", [])

    # Add new message
    logs.append(f"{user}: {text}")

    # Limit sa last 10 lang
    if len(logs) > MAX_LOGS:
        logs = logs[-MAX_LOGS:]

    context.chat_data["message_logs"] = logs


async def show_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ipakita ang last 10 messages."""
    logs = context.chat_data.get("message_logs", [])

    if not logs:
        await update.message.reply_text("📭 Wala pang na-log na message.")
        return

    history_text = "\n".join(logs)
    await update.message.reply_text(f"🕓 Last {len(logs)} Messages:\n\n{history_text}")
