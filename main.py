import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from Bot.store_bot.handlers.cmd_handlers import cmd_router
from Bot.store_bot.handlers.maxsulot_handlers import maxsulot_router
from Bot.store_bot.handlers.product_handler import product_router
from config import BOT_TOKEN



async def main():
    bot = Bot(
        token=BOT_TOKEN,
        parse_mode=ParseMode.HTML
    )
    dp = Dispatcher()
    dp.include_routers(cmd_router, maxsulot_router, product_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print('Bot to\'xtatildi')