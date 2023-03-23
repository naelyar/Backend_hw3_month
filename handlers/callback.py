from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_2)
    question = "When is my birthday?"
    answer = [
        "05.06.05",
        "06.06.06",
        "23.10.79",
        "10.06.05"
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
)
async def quiz_3(call: types.CallbackQuery):
    question = "How to called film?"
    answer = [
        "Classmates",
        "Harry Potter",
        "Get the knives"
    ]
    photo = open('media/100x64_3.jpg', 'rb')
    await bot.send_photo(call.from_user.id,photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        type='quiz',
        correct_option_id=2
)
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")