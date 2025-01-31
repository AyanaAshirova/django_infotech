import asyncio
from TeleBot.bot import main

if __name__ == "__main__":
    asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_forever()