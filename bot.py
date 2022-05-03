from create_bot import bot, dp
from aiogram.utils import executor

def add_handlers():
    from app.handlers.common import register_common_hadlers
    register_common_hadlers(dp)

if __name__ == "__main__":
    add_handlers()
    executor.start_polling(dp, skip_updates=True)