from aiogram import Bot
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery, Message
from utils.env import env
from asyncio import create_task



async def check_channel_task(query: CallbackQuery, bot: Bot):
    user_status = await bot.get_chat_member(env.str('CHANNEL_ID'), query.from_user.id)
    if user_status.status in ['member', 'administrator', 'creator']:
        await query.message.delete()
    else:
        await query.answer("Siz kanalga obuna bo'lmagansiz, iltimos, kanalga obuna bo'ling va qayta urinib ko'ring.")

async def check_channel(query: CallbackQuery, bot: Bot):
    await create_task(check_channel_task(query, bot))
