from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data import users, get_user_ball
from states import get_user_realy_name
from keyboard import main_menu

async def start_command_answer(message: Message, state: FSMContext):
    if message.text[7:].isdigit():
        if users.get(str(message.from_user.id)):
            if int(message.text[7:]) == message.from_user.id:
                await message.answer(f"Hurmatli {message.from_user.first_name}!\n Siz O'zingizga referal bo'lishhga urinyapsiz ❌")
            else:
                await message.answer("Siz botga oldin tashrif buyurgansiz va referal bo'la olmaysiz ! 💸")
        else:
            reffer_id = message.text[7:]
            users[str(message.from_user.id)] = {'reffer_id': reffer_id, 'flag': False}

            await state.set_state(get_user_realy_name.name)
            await message.answer("📲Botdan ro'yhatdan o'tish ushun \n\n Ismingizni kiriting:")
    else:
        if users.get(str(message.from_user.id)):
            if users.get(str(message.from_user.id)).get('user_realy_name'):
                await message.answer('Asosiy Menyudasiz!🎉', reply_markup=main_menu)
            else:
                await message.answer("📲Botdan ro'yhatdan o'tish ushun \n\n Ismingizni kiriting:")
        else:
            users[str(message.from_user.id)] = {'reffer_id': None, 'flag': False}

            await state.set_state(get_user_realy_name.name)
            await message.answer("📲Botdan ro'yhatdan o'tish ushun \n\n Ismingizni kiriting:")

async def get_user_realy_name_answer(message: Message, state: FSMContext):
    users[str(message.from_user.id)]["user_realy_name"] = message.text
    users[str(message.from_user.id)]["flag"] = True
    await message.answer(f"✅ {message.text} siz muvaffaqiyatli Ro'yhatdan o'tdingiz\n\n Siz Asosiy Menyudasiz!🎉", reply_markup=main_menu)
    await state.clear()


async def get_ref_link_answer(message: Message, state: FSMContext):
    if users.get(str(message.from_user.id)):
        ref_link = f"https://t.me/testuchforbot?start={message.from_user.id}"
        await message.answer(f"Sizning referal havolangiz:\n\n{ref_link}")
    else:
        users[str(message.from_user.id)] = {'reffer_id': None, 'flag': False}
        await state.set_state(get_user_realy_name.name)
        await message.answer("📲 Botdan ro'yhatdan o'tish ushun \n\n Ismingizni kiriting:")

async def get_user_ball_answer(message: Message, state: FSMContext):
    if users.get(str(message.from_user.id)):
        user_ball = get_user_ball(str(message.from_user.id))
        await message.answer(f'👤 Takliflaringiz soni: {user_ball} ta')
    else:
        users[str(message.from_user.id)] = {'reffer_id': None, 'flag': False}
        await state.set_state(get_user_realy_name.name)
        await message.answer("📲Botdan ro'yhatdan o'tish ushun \n\n Ismingizni kiriting:")

