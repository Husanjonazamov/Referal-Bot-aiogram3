from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data import users, get_user_ball
from States.states import get_user_realy_name
from asyncio import create_task



async def get_user_ball_answer_task(message: Message, state: FSMContext):
    if users.get(str(message.from_user.id)):
        user_ball = get_user_ball(str(message.from_user.id))
        await message.answer(f'👤 Takliflaringiz soni: {user_ball} ta')
    else:
        users[str(message.from_user.id)] = {'reffer_id': None, 'flag': False}
        await state.set_state(get_user_realy_name.name)
        await message.answer("📲Botdan ro'yhatdan o'tish ushun \n\n Ismingizni kiriting:")


async def get_user_ball_answer(message: Message, state: FSMContext):
    await create_task(get_user_ball_answer_task(message, state))