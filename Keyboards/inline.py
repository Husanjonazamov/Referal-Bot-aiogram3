from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




channel_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🕹 1-kanal", callback_data="1", url='https://t.me/testforkna'),
        ],
        [
            InlineKeyboardButton(text="✅ Tekshirish", callback_data="check"),
        ]
    ]
)

