from telegram import Update
from telegram.ext import ContextTypes

import api


async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"👋 Добро пожаловать, {user_name}!")


async def get_top_headlines(update: Update, context: ContextTypes.DEFAULT_TYPE):
    top_headlines = api.get_top_headlines()

    if top_headlines is None:
        return

    message = ""
    for headline in top_headlines:
        title = headline["title"]
        author = headline["author"]
        description = headline["description"]
        url = headline["url"]
        message += f"{title}\n\n{author}\n{description}\n\nПодробнее: {url}\n\n-----------------\n\n"

    await update.message.reply_text(message)
