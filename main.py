from aiogram import Bot, Dispatcher, types
import asyncio
import common
# Ваш токен от BotFather
API_TOKEN = '7541209056:AAHQd9Qv_ljTbP7zfIumTdKhycC1zCfFpDI'

    
async def main():
    
    dp = Dispatcher()
    bot = Bot(token=API_TOKEN)
    

    dp.include_router(common.router)
    
    await dp.start_polling(bot)
# Запуск бота   
if __name__ == '__main__':
    asyncio.run(main())
