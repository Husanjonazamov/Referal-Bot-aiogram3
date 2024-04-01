from aiogram import Bot, Dispatcher, F
from asyncio import run
from aiogram.filters import CommandStart
import funcs
import states

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(5765144405, "✅ Bot ishga tushdi")

async def shutdown_answer(bot: Bot):
    await bot.send_message(5765144405, "❌ Bot ishdan to'xtadi")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(funcs.start_command_answer, CommandStart())
    dp.message.register(funcs.get_user_realy_name_answer, states.get_user_realy_name.name)
    dp.message.register(funcs.get_ref_link_answer, F.text == '💵Referal Havola')
    dp.message.register(funcs.get_user_ball_answer, F.text == '💰Mening Takliflarim')
    bot = Bot('7178118588:AAHMuun6LvJ4lyjObeo7n_S_WmC_H45pWfI')
    await dp.start_polling(bot, polling_timeout=1)

run(start())