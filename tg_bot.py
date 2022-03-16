from ast import Call
from operator import truediv
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
import logging
from dotenv import load_dotenv
import os
import data_management as dm


load_dotenv()

updater = Updater(token=os.getenv("TG_TOKEN"), use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)


def get_alerts_str():
    items_list_str = map(
        lambda item: f"[{item['name']}]({item['url']})", dm.json_object
    )
    return "\n".join(items_list_str)


def list_alert(update: Update, context: CallbackContext):
    context.bot.send_message(
        update.effective_chat.id,
        get_alerts_str(),
        parse_mode="MarkdownV2",
        disable_web_page_preview=True,
    )


list_alerts_handler = CommandHandler("alerts", list_alert)
dispatcher.add_handler(list_alerts_handler)

updater.start_polling()
