from telegram import Update, ChatPermissions
from telegram.ext import ContextTypes
import time

ADMIN_ONLY_MODE = False


async def adminonly(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ADMIN_ONLY_MODE

    user = update.effective_user
    chat = update.effective_chat

    member = await chat.get_member(user.id)
    if not member.status in ["administrator", "creator"]:
        await update.message.reply_text("🚫 Only admins can toggle Admin-Only mode.")
        return

    ADMIN_ONLY_MODE = not ADMIN_ONLY_MODE
    state = "✅ ON" if ADMIN_ONLY_MODE else "❌ OFF"
    await update.message.reply_text(f"🔒 Admin-Only mode is now *{state}*.", parse_mode="Markdown")


async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    member = await chat.get_member(user.id)

    # Only admin can mute
    if not member.status in ["administrator", "creator"]:
        await update.message.reply_text("🚫 Only admins can use /mute.")
        return

    # Must reply to someone
    if not update.message.reply_to_message:
        await update.message.reply_text("❗ Reply to a message to mute that user.")
        return

    target_user = update.message.reply_to_message.from_user

    try:
        duration = int(context.args[0]) if context.args else 60  # default 60 seconds
        until_date = int(time.time() + duration)

        await context.bot.restrict_chat_member(
            chat_id=chat.id,
            user_id=target_user.id,
            permissions=ChatPermissions(can_send_messages=False),
            until_date=until_date,
        )

        await update.message.reply_text(f"🔇 {target_user.mention_html()} has been muted for {duration} seconds.",
                                        parse_mode="HTML")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")


async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    member = await chat.get_member(user.id)

    if not member.status in ["administrator", "creator"]:
        await update.message.reply_text("🚫 Only admins can use /ban.")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("❗ Reply to a message to ban that user.")
        return

    target_user = update.message.reply_to_message.from_user

    try:
        await context.bot.ban_chat_member(chat.id, target_user.id)
        await update.message.reply_text(f"🚫 {target_user.mention_html()} has been *banned* from the group.",
                                        parse_mode="HTML")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")