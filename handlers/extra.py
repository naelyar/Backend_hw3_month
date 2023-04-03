from aiogram import types, Dispatcher
from config import bot, ADMINS

import random
async def pinText(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
async def gameEmoji(message:types.Message):
    if message.text.startswith("game") and message.from_user.id in ADMINS:
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽️', '🏀']
        dice = random.choice(emojis)
        await message.answer(dice)

async  def squaringAndEcho(message: types.Message):
    if message.text.isdigit():
        numbers = int(message.text)
        await message.answer(f"{numbers ** 2}")

    else:
            await bot.send_message(chat_id=message.from_user.id, text=message.text)
def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(pinText)
    dp.register_message_handler(gameEmoji)
    dp.register_message_handler(squaringAndEcho)

