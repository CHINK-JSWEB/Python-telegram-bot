from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("ℹ️ About", callback_data="about")],
        [InlineKeyboardButton("🆘 Help", callback_data="help")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact")]
    ]
    return InlineKeyboardMarkup(keyboard)
