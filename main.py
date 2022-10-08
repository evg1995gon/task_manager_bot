import os
import logging
from dotenv import load_dotenv

import db
import logic

load_dotenv()
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = os.getenv('BOT')


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    logic.add_member(message.from_id, message.from_user.username)
    await message.answer(
        "Привет!\nЯ бот для сохранения заметок!\n\n"
        "   Для того чтобы добавить заметку напишите: добавить ...\n\n"
        "   Для того чтобы удалить заметку напишите: удалить ...\n\n"
        "   Для того чтобы увидеть список ваших дел напишите: список")

# @dp.message_handler(commands=['del'])
# async def send_welcome(message: types.Message):
#
#     logic.add_member(message.from_id, message.from_user.username)
#     await message.answer(
#         "Привет!\nЯ бот для сохранения заметок!\n\n"
#         "   Для того чтобы добавить заметку напишите: добавить ...\n\n"
#         "   Для того чтобы увидеть список ваших дел напишите: список")

@dp.message_handler()
async def message_handler(message: types.Message):
    answer = logic.parsing_massage(message.text, message.from_id)
    if type(answer) == str:
        await message.answer(answer)
    else:
        await message.answer('Ваш список: ')
        for x in answer:
            await message.answer(x + ' /del' + str(db.get_id_text(x)))
        await message.answer('Судя по вашему списку вы грязное чудовище')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)