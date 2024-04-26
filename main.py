'''
asinchro telegram bot
'''

import asyncio
import logging
import sys

from asyncio.log import logger
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers import rt
from app.db.models import async_main

TOKEN = '6764742756:AAF2zhN7-6uSLksUvCnoonyWkmA94oStQTA'


async def main() -> None:
    '''
    запускатель всего
    '''
    await async_main()
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(rt)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Bot off')
    except asyncio.exceptions.CancelledError:
        logger.info('Bot off2')
