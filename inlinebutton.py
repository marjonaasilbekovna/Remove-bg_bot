from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

colors_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Oq", callback_data="white"), InlineKeyboardButton(text="Qora", callback_data="black")],
        [InlineKeyboardButton(text="Sariq", callback_data="yellow"), InlineKeyboardButton(text="To'q sariq", callback_data="orange")],
        [InlineKeyboardButton(text="Ko'k", callback_data="blue"), InlineKeyboardButton(text="To'q ko'k", callback_data="dark blue")],
        [InlineKeyboardButton(text="Pushti", callback_data="pink"), InlineKeyboardButton(text="Qizil", callback_data="red")],
        [InlineKeyboardButton(text="Yashil", callback_data="green"), InlineKeyboardButton(text="To'q yashil", callback_data="dark green")]
    ]
)
