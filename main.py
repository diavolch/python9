import complex
import racional
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="TOKEN_API")
dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
    a = State()
    b = State()
    move = State()

@dp.message_handler(commands='start')
async def get_message(message: types.Message):
    await Form.a.set()
    await message.answer(text='Введите первое число:')

@dp.message_handler(state=Form.a)
async def process_a(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['a'] = message.text
    await Form.next()
    await message.reply('Введите второе число:')

@dp.message_handler(state=Form.b)
async def process_b(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(b=message.text)
    await message.reply('Какое действие необходимо совершить?')

@dp.message_handler(state=Form.move)
async def process_move(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['move'] = message.text
    if 'j' in data['a']:
        result = complex.complex_result(data['a'], data['b'], data['move'])
        await bot.send_message(
            message.chat.id,
            result)
    else:
        result = racional.racional_result(data['a'], data['b'], data['move'])
        await bot.send_message(
            message.chat.id,
            result)
    await state.finish()


executor.start_polling(dp)
