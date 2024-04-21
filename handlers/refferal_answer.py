from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from States.states import get_user_realy_name
from data import users
from asyncio import create_task


async def get_ref_link_answer_task(message: Message, state: FSMContext):
    if users.get(str(message.from_user.id)):
        ref_link = f"https://t.me/testuchforbot?start={message.from_user.id}"
        await message.answer(f"Sizning referal havolangiz:\n\n{ref_link}")
    else:
        users[str(message.from_user.id)] = {'reffer_id': None, 'flag': False}
        await state.set_state(get_user_realy_name.name)
        await message.answer("📲 Botdan ro'yhatdan o'tish ushun \n\n Ismingizni kiriting:")


async def get_ref_link_answer(message: Message, state: FSMContext):
    await create_task(get_ref_link_answer_task(message, state))