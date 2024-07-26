import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from aiogram_dialog import setup_dialogs
from environs import Env
from redis.asyncio.client import Redis

import handlers.handlers
from config.config import (
    BOT_TOKEN,
    PARSE_MODE,
    REDIS_HOST,
    REDIS_PASSWORD,
    REDIS_PORT,
)
from dialogs.bank_card_dialog import bank_card
from dialogs.faq_dialog import faq_dialog
from dialogs.main_menu import main_menu
from dialogs.transport_card_dialog import transport_card


async def main() -> None:
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode[PARSE_MODE]),
    )

    storage = RedisStorage(
        Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD),
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )
    dp = Dispatcher(storage=storage)

    router = Router()

    dp.include_router(router)
    dp.include_router(handlers.handlers.router)
    dp.include_routers(main_menu, bank_card, transport_card, faq_dialog)
    setup_dialogs(dp)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
