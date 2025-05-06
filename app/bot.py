from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler
)

from config import get_telegram_token
from handlers import say_hello, get_top_headlines


def start_bot():
    token = get_telegram_token()

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", say_hello))
    app.add_handler(CommandHandler("get_top_headlines", get_top_headlines))

    app.run_polling(allowed_updates=Update.ALL_TYPES)
