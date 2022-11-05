import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import logic
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
API_TOKEN = os.getenv('BOT')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

button_list = KeyboardButton('Список')
button_delete_all = KeyboardButton('Удалить все')


just_list = ReplyKeyboardMarkup(resize_keyboard=True).add(button_list).add(button_delete_all)
# just_delete = ReplyKeyboardMarkup(resize_keyboard=True).add(button_delete_all)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    logic.add_member(message.from_id, message.from_user.username)
    await message.answer(
        "Привет!\nЯ бот для сохранения заметок!\n\n"
        "   Для того чтобы добавить заметку напишите: добавить ...\n\n"
        "   Для того чтобы увидеть список ваших дел напишите: список\n\n"
        "   Для того чтобы удалить заметку напишите: удалить ...\n"
        "   Для того чтобы очистить список напишите: удалить все\n\n",
        reply_markup=just_list)


@dp.message_handler()
async def message_handler(message: types.Message):
    answer = logic.parsing_massage(message.text, message.from_id)
    if type(answer) == str:
        await message.answer(answer)
    elif answer == None:
        await message.answer('Ваш список пуст   /start')
    else:
        if answer == []:
            await message.answer('Ваш список пуст   /start')
        else:
            await message.answer('Ваш список: ')
            for x in answer:
                # await message.answer(x + ' /del' + str(db.get_id_text(x)))
                await message.answer(x)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)