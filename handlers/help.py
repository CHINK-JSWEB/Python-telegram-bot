from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# --- Main Help Menu ---
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🎮 Fun", callback_data="help_fun"),
            InlineKeyboardButton("⚙️ Utilities", callback_data="help_utils")
        ],
        [
            InlineKeyboardButton("👮 Admin Tools", callback_data="help_admin")
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="back_to_main")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        text="📚 *Help Menu*\n\nPili ng category para makita ang mga available na commands 👇",
        reply_markup=reply_markup, parse_mode="Markdown"
    )


# --- Fun Commands ---
async def help_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("😂 /joke", callback_data="cmd_joke"),
            InlineKeyboardButton("📸 /meme", callback_data="cmd_meme")
        ],
        [
            InlineKeyboardButton("💬 /quote", callback_data="cmd_quote")
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="help_main")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        text="🎮 *Fun Commands*\nPiliin ang gusto mong subukan:",
        reply_markup=reply_markup, parse_mode="Markdown"
    )

# --- Utilities Commands ---
async def help_utils(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🆔 /id", callback_data="cmd_id"),
            InlineKeyboardButton("🕒 /time", callback_data="cmd_time")
        ],
        [
            InlineKeyboardButton("📜 /history", callback_data="cmd_history")
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="help_main")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        text="⚙️ *Utilities Commands*\nPiliin ang gusto mong gamitin:",
        reply_markup=reply_markup, parse_mode="Markdown"
    )

# --- Admin Commands ---
async def help_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🔒 /adminonly", callback_data="cmd_adminonly"),
            InlineKeyboardButton("🔇 /mute", callback_data="cmd_mute")
        ],
        [
            InlineKeyboardButton("🚫 /ban", callback_data="cmd_ban")
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data="help_main")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(
        text="👮 *Admin Tools*\nPiliin ang admin command:",
        reply_markup=reply_markup, parse_mode="Markdown"
    )
