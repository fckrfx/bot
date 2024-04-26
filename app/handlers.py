'''
handlers live here
'''

import webbrowser

from aiogram import F, html, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb
import app.db.requests as rq

rt = Router()


class Registrator(StatesGroup):
    '''
    класс регистратора юзеров
    '''
    name = State()
    age = State()
    phone = State()


@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    '''
    handler обрабатывает комманду `/start`
    '''
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!",  # type: ignore
        reply_markup=kb.rk01,
    )


@rt.message(F.text == 'SignUp')
async def sign(message: Message, state: FSMContext) -> None:
    '''
    handler обрабатывает текст `SignUp`
    спрашивает имя юзера
    '''
    await state.set_state(Registrator.name)
    await message.answer('Input your name:', reply_markup=kb.rm)


@rt.message(Registrator.name)
async def reg_name(message: Message, state: FSMContext) -> None:
    '''
    handler сохраняет имя
    спрашивает возраст
    '''
    await state.update_data(name=message.text)
    await state.set_state(Registrator.age)
    await message.answer('Input your age:')


@rt.message(Registrator.age)
async def reg_age(message: Message, state: FSMContext) -> None:
    '''
    handler сохраняет возраст
    спрашивает телефон
    '''
    await state.update_data(age=message.text)
    await state.set_state(Registrator.phone)
    await message.answer('Share your phone number:', reply_markup=kb.rk02)


@rt.message(Registrator.phone, F.contact)
async def reg_phone(message: Message, state: FSMContext) -> None:
    '''
    handler записывает инфо в бд
    выводит инфо о юзере
    '''
    await state.update_data(phone=message.contact.phone_number)  # type: ignore
    data = await state.get_data()
    await message.answer(
        f'Имя:{data['name']}\nВозраст:{data['age']}\nТелефон:{data['phone']}',
        reply_markup=kb.rm)
    await state.clear()


@rt.message(F.text == 'view menu')
async def menu(message: Message) -> None:
    '''
    handler обрабатывает текст `view menu`
    '''
    await message.answer('You chose MENU. Here it is:',
                         reply_markup=kb.ik01)


@rt.callback_query(F.data == 'ibut00')
async def ibut00(callback: CallbackQuery) -> None:
    '''
    handler обрабатывает текст `ibut00`
    '''
    await callback.answer('u pushed IBUT00',
                          show_alert=True)


@rt.message(F.text == 'hurra')
async def hurra(message: Message) -> None:
    '''
    handler обрабатывает текст `hurra`
    '''
    await message.reply('best wishes!')


@rt.message(Command('chat'))
async def command_message_handler(message: Message) -> None:
    '''
    handler обрабатывает комманду `/chat`
    '''
    await message.reply(f'{message.chat}')


@rt.message(Command('user'))
async def command_user_handler(message: Message) -> None:
    '''
    handler обрабатывает комманду `/user`
    '''
    await message.reply(f'{message.from_user}')


@rt.message(Command('yura'))
async def command_yura_handler(message: Message) -> None:
    '''
    handler обрабатывает комманду `yura'
    '''
    await message.reply('open ya.ru in your browser')
    webbrowser.open('https://ya.ru', 2)


@rt.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender
    By default, message handler will handle all message types
      (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(
            chat_id=message.chat.id,
            reply_to_message_id=message.message_id)
        await message.reply_dice('🎲')
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")
