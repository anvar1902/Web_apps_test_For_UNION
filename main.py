from aiogram import Bot, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters.command import Command
import asyncio

bot = Bot("7087738518:AAHlbhjjopmRndLecg6eQyN-GmwXWIgtWFg")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Открыть кликер", web_app=WebAppInfo(url="https://anvar1902.github.io/Web_apps_test_For_UNION/"))]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )
    await message.answer(text="Привет, я бот, который умеет отвечать на вопросы Вроде бы но после того как я написал Вроде бы ещё и с большой буквы уже пишет создатель а не рандом хуитас", reply_markup=keyboard)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())