from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from database.bot_db import  sql_command_insert
class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    position = State()
    age = State()
    group = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.id.set()
        await message.answer("Как зовут?")
        await FSMAdmin.next()

    else:
        await message.answer("!!!")
async def load_name(message: types.Message, state: FSMContext):
   async with  state.proxy() as data:
       data['id'] = message.from_user.id
       data['name'] = message.text
   await FSMAdmin.next()
   await message.answer("Направление")
async def load_position(message: types.Message, state: FSMContext):
   async with  state.proxy() as data:
       data['position'] = message.text
   await FSMAdmin.next()
   await message.answer("Возраст")
async def load_age(message: types.Message, state: FSMContext):
   async with  state.proxy() as data:
       if not message.text.isdigit():
           await  message.answer("Пиши числами")
       data['age'] = message.text
   await FSMAdmin.next()
   await message.answer("Группа")
async def load_group(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
      await  message.answer("Пиши числами")
    async with  state.proxy() as data:
           data['group'] = message.text
           await  message.answer(f"Твои данные:\n Имя:{data['name']}\n Направление:{data['position']}\n"
                                 f" Возраст:{data['age']}\n Группа:{data['group']}\n Твой Id в секрете )))")
    await FSMAdmin.next()
    await message.answer("Все данные верны?")
async def submit(message: types.Message, state:FSMContext):
    if message.text == "Да":
        await  sql_command_insert(state)
        await state.finish()
        await message.answer("Ты зареган!")
    elif message.text == 'Нет':
        await state.finish()
        await message.answer("Ну и ладно!")
    else:
        await  message.answer("!")

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено")
def register_handlers_fsmAdminMentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(cancel_reg, Text(equals="cancel", ignore_case=True), state='*')
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_position, state=FSMAdmin.position)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)

