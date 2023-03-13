from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

"""Command start"""
@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer("Hello Naelya")

"""First quiz"""
@dp.message_handler(commands=['quiz1'])
async def quiz_1(message: types.Message):
    question = "Date  of based GeekTech"
    answer = [
        "05.2018",
        "06.2016",
        "12.2022",
        "04.2021"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=5
    )

"""Second quiz"""
@dp.message_handler(commands=['quiz2'])
async def quiz_2(message: types.Message):
    question = "When is my birthday?"
    answer = [
        "05.06.05",
        "06.06.06",
        "23.10.79",
        "10.06.05"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        type='quiz',
        correct_option_id=2
)
"""Sending mem"""

@dp.message_handler(commands=['mem'])
async def sendMem(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://cs14.pikabu.ru/post_img/2022/08/27/10/1661620223122060416.jpg")

"""Squaring and Echo"""
@dp.message_handler()
async  def squaringAndEcho(message: types.Message):
    if message.text.isdigit():
        numbers = int(message.text)
        await message.answer(f"{numbers ** 2}")
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


