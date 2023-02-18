import logging

from aiogram import Bot, Dispatcher, executor, types

import inline_keyboard
import messages
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'weather'])
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather(),
                         reply_markup=inline_keyboard.WEATHER)



@dp.callback_query_handler(text='mitte')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weatherMitte(),
        reply_markup=inline_keyboard.WEATHER
    )

@dp.callback_query_handler(text='moscow')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weatherMoscow(),
        reply_markup=inline_keyboard.WEATHER
    )

@dp.callback_query_handler(text='kyiv')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weatherKyiv(),
        reply_markup=inline_keyboard.WEATHER
    )

@dp.callback_query_handler(text='istanbul')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weatherIstanbul(),
        reply_markup=inline_keyboard.WEATHER
    )

@dp.callback_query_handler(text='new_york')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weatherNew_York(),
        reply_markup=inline_keyboard.WEATHER
    )

@dp.callback_query_handler(text='tashkent')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.weather(),
        reply_markup=inline_keyboard.WEATHER
    )




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)