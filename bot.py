from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

API_TOKEN = "ТОКЕН_ТВОЕГО_БОТА"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(url="https://твой-домен.ru/profile")
    keyboard.add(types.InlineKeyboardButton(text="🚀 Запуск", web_app=web_app))

    await message.answer(
        "Привет! Нажми кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
