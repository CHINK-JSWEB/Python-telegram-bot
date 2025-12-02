# keyboard/main_menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🆘 Help", callback_data="help")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact")]
    ]
    return InlineKeyboardMarkup(keyboard)


def help_main_keyboard():
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
    return InlineKeyboardMarkup(keyboard)


def help_fun_keyboard():
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
    return InlineKeyboardMarkup(keyboard)


def help_utils_keyboard():
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
    return InlineKeyboardMarkup(keyboard)


def help_admin_keyboard():
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
    return InlineKeyboardMarkup(keyboard)
