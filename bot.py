# Подключение библиотек
import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types

# Переменные с токеном бота и сообщением, которое он будет отправлять пользователю
TOKEN = "ваш токен"
MSG = "Ты можешь задать новый вопрос, {}"

logging.basicConfig(level=logging.INFO)

# Создание экземпляра класса Bot, передача ему в качестве аргумента токена , и экземпляра класса Dispatcher (dp),
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=["start"])

#Функция, которая будет обрабатывать команду /start и определяет логику, в соответствии с которой будет работать бот.
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")


    for i in range(1):
        await asyncio.sleep(5)
        await bot.send_message(user_id, MSG.format(user_name))


if __name__ == "__main__":
    executor.start_polling(dp)
