from googletrans import Translator
from aiogram import types, Dispatcher
# print(googletrans.LANGUAGES)

translator = Translator()
async def translate_text(message: types.Message):
    text_to_translate = message.get_args()
    print(f"Переводим текст: {text_to_translate}")
    translated_text = translator.translate(text_to_translate, src="ru", dest="en").text
    print(f"Получили перевод: {translated_text}")
    await message.answer(translated_text)

def register_handlers_translater(dp: Dispatcher):
    dp.register_message_handler(translate_text, commands=['translate'])
