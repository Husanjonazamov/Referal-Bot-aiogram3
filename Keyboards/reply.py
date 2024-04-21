from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💵Referal Havola'),
            KeyboardButton(text='💰Mening Takliflarim'),
        ]
    ],
    resize_keyboard=True,
    is_persistent=True
)