from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.bot_db import sql_command_random
from parser.film import parsers
async def start_command(message:types.Message):
    await message.answer("Hello Naelya")

"""First quiz"""
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)
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
        open_period=5,
        reply_markup=markup
    )

"""Sending mem"""
async def sendMem(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://cs14.pikabu.ru/post_img/2022/08/27/10/1661620223122060416.jpg")
async def help_command(message: types.Message):
    photo = open('media/02.png', 'rb')
    await message.answer_photo(photo=photo, caption='No')
async def get_random_user(message: types.Message):
    random_user = await sql_command_random()
    await message.answer_photo(
        photo=random_user[-1],
        caption=f"{random_user[2]} {random_user[3]} {random_user[4]} {random_user[5]}\n"
                f"@{random_user[1]}\n Твой Id в секрете )))")

async def get_films(message: types.Message):
    films = parsers()
    for film in films:
        await message.answer(
            f"{film['title']}\n\n"
            f"<b><a href='{film['link']}'>{film['title']}</a></b>\n"
            f"{film['year']}\n"
            f"{film['genre']}\n"
            f"{film['country']}\n"
        )
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz_1'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(get_films, commands=['films'])



