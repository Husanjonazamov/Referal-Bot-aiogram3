from aiogram import Bot, Dispatcher, F
from asyncio import run
from aiogram.filters import CommandStart
from States import states
from utils.env import env
from handlers import start_command, get_user_ball, refferal_answer
from subscribe_channel import is_channels, channel_callback



dp = Dispatcher()

bot = Bot(env.str('BOT_TOKEN'))


async def startup_answer(bot: Bot):
    await bot.send_message(5765144405, "✅ Bot ishga tushdi")

async def shutdown_answer(bot: Bot):
    await bot.send_message(5765144405, "❌ Bot ishdan to'xtadi")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.message.register(is_channels.sub_channel, is_channels.CheckSubChannel()),
    dp.callback_query.register(channel_callback.check_channel, F.data.lower() == 'check')
    dp.message.register(start_command.start_command_answer, CommandStart()),
    dp.message.register(start_command.get_user_realy_name_answer, states.get_user_realy_name.name),
    dp.message.register(refferal_answer.get_ref_link_answer, F.text == '💵Referal Havola'),
    dp.message.register(get_user_ball.get_user_ball_answer, F.text == '💰Mening Takliflarim'),
    await dp.start_polling(bot, polling_timeout=1)

run(start())