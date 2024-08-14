from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

router = Router()

@router.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    # Создаем инлайн-кнопку с ссылкой на ваше веб-приложение
    webapp_button = InlineKeyboardButton(text="Перейти", web_app=WebAppInfo(url='https://lonelou526.github.io/happy_birthday.html'))


    
    # Добавляем кнопку в инлайн-клавиатуру
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[webapp_button]])
    
    # Отправляем сообщение с кнопкой
    await message.reply("Привет!!!!!! Мне было нечего делать, и я решил перенести сайт в маленького бота.\nКстати учти, что каждый раз, когда ты будешь заходить в него, мне будет приходить сообщение)", reply_markup=keyboard)
   