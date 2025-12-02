from telegram import Update
from telegram.ext import ContextTypes
from handlers.start import start
from handlers.help import help_command, help_fun, help_utils, help_admin

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    # Main Menus
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

    # Help categories
    elif data == "help_fun":
        await help_fun(update, context)
    elif data == "help_utils":
        await help_utils(update, context)
    elif data == "help_admin":
        await help_admin(update, context)

    # --- Command Info Sections ---
    # Fun
    elif data == "cmd_joke":
        await query.edit_message_text("😂 *Command:* `/joke`\nSends a random joke!", parse_mode="Markdown")
    elif data == "cmd_meme":
        await query.edit_message_text("📸 *Command:* `/meme`\nSends a random meme!", parse_mode="Markdown")
    elif data == "cmd_quote":
        await query.edit_message_text("💬 *Command:* `/quote`\nSends an inspirational quote.", parse_mode="Markdown")

    # Utilities
    elif data == "cmd_id":
        await query.edit_message_text("🆔 *Command:* `/id`\nShows your Telegram ID.", parse_mode="Markdown")
    elif data == "cmd_time":
        await query.edit_message_text("🕒 *Command:* `/time`\nShows the current server time.", parse_mode="Markdown")
    elif data == "cmd_history":
        await query.edit_message_text("📜 *Command:* `/history`\nDisplays the last 10 messages from chat.", parse_mode="Markdown")

    # Admin
    elif data == "cmd_adminonly":
        await query.edit_message_text("🔒 *Command:* `/adminonly`\nEnables admin-only mode — only admins can use commands.", parse_mode="Markdown")
    elif data == "cmd_mute":
        await query.edit_message_text("🔇 *Command:* `/mute`\nTemporarily mutes a user.", parse_mode="Markdown")
    elif data == "cmd_ban":
        await query.edit_message_text("🚫 *Command:* `/ban`\nBans a user from the group.", parse_mode="Markdown")
