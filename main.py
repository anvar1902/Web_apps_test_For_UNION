import logging
import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot("7087738518:AAHlbhjjopmRndLecg6eQyN-GmwXWIgtWFg")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [
        [types.InlineKeyboardButton(text="Открыть кликер", web_app=WebAppInfo(url="https://anvar1902.github.io/Web_apps_test_For_UNION"))]
    ]

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=kb
    )
    await message.answer(text="Привет, я бот, который умеет отвечать на вопросы Вроде бы но после того как я написал Вроде бы ещё и с большой буквы уже пишет создатель а не рандом хуитас", reply_markup=keyboard)

dp.message(content_types=["web_app_data"])
async def web_app_update(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(res)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())