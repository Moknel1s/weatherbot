from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')

MITTE = InlineKeyboardButton('Mitte', callback_data='mitte')
MOSCOW = InlineKeyboardButton('Moscow', callback_data='moscow')
KYIV = InlineKeyboardButton('Pushcha-Vodytsya', callback_data='kyiv')
ISTANBUL = InlineKeyboardButton('Karaköy', callback_data='istanbul')
NEW_YORK = InlineKeyboardButton('Long Island City', callback_data='new_york')
TASHKENT = InlineKeyboardButton('Tashkent', callback_data='tashkent')

WEATHER = InlineKeyboardMarkup().add(MITTE, MOSCOW, KYIV, ISTANBUL, NEW_YORK, TASHKENT)

