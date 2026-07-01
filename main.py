import asyncio

from bot.client import MyBot
from bot.core.config import settings
from bot.core.logging import setup_logging


async def main():
    setup_logging()
    bot = MyBot()
    async with bot:
        await bot.start(settings.TOKEN)


if __name__ == "__main__":
    asyncio.run(main())