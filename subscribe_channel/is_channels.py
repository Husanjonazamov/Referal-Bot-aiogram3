from aiogram.filters import Filter
from aiogram import Bot
from aiogram.types import Message
from utils.env import env
from Keyboards.inline import channel_menu
from asyncio import create_task



class CheckSubChannel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        user_status = await bot.get_chat_member(env.str('CHANNEL_ID'), message.chat.id)
        if user_status.status in ['member', 'administrator', 'creator']:
            return False
        else:
            return True

async def sub_channel_task(message: Message, bot: Bot):
    text = message.text
    channel_test = await message.answer(f"Bot to'liq ishlashi uchun pastdagi kanallarga obuna bo'ling", reply_markup=channel_menu)


async def sub_channel(message: Message, bot: Bot):
    await create_task(sub_channel_task(message, bot))

