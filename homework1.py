from aiogram.utils import executor
from config import dp, bot, ADMINS
import logging
from handlers import callback, fsmAdminMentor, extra, schedule, translater
from database.bot_db import sql_create
async def on_startup(_):
    await schedule.set_scheduler()
    await bot.send_message(ADMINS[0], "I started")
    sql_create()
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsmAdminMentor(dp)
extra.register_handlers_extra(dp)
translater.register_handlers_translater(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


