import asyncio
import datetime
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Active logging
logging.basicConfig(level=logging.INFO)
# Object of the bot
bot = Bot(token="7381066612:AAFvkIQ6jW_gjEyAiPxsFZ7yhidp_Pnsngk")
# Dispatcher
dp = Dispatcher()

# Command /start
@dp.message(Command("start"))
async def start(message: Message):
	await message.answer("Hello, I'm bot")
	await message.answer("/commands - узнать все комманды данного бота")

# Command /helpme
@dp.message(Command("helpme"))
async def help(message: Message):
	keyboard = InlineKeyboardMarkup()
	buttons = InlineKeyboardButton(text="Мой Tg канал",
									url="https://t.me/+JGKYwKNHx9c4Njgy")
	keyboard.add(buttons)
	await message.answer("Добро пожаловать! Нажмите на кнопку ниже:", reply_markup=keyboard)

"""
# Command /time
@dp.message(Command("time"))
async def nowtime(message: Message):
	time=datetime.time()
	await message.reply(time=time)"""

#
@dp.message(Command("commands"))
async def commands(message: Message):
	await message.answer("/start - Выводит приветствие бота")
	await message.answer("/helpme - Выводит ссылки на контакты создателя")

# The function repeat inputed text
@dp.message()
async def echo(message: Message):
	await message.reply(text=message.text)

# The main function
async def main():
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())