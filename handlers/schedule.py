import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.bot_db import sql_command_all_id
from apscheduler.triggers.cron import CronTrigger
from config import  bot

async def reminder(bot: Bot):
    user_ids = await sql_command_all_id()
    for user_id in user_ids:
        await bot.send_message(user_id[0], "Call A.")
async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(reminder, trigger=CronTrigger( year=2023, month=6, day=10, hour=21, minute=56),
                      kwargs={"bot": bot})

    scheduler.start()