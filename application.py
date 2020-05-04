import os
import logging

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Минмиальный сценарий: 
# - на каждый чих пользователя бот говорит "Я что-то слышу!"

# Ограничения:
# - все делается последовательно, нет аснихронности / балансировщика
# - мы не храним состояние бот и не храним историю сообщений


# Webhook-вариант:
# 1. приложение на Flask должно обрабтывать на входе запрос POST от Telegram 
#    на своем endpoint'е
# 2. по результатам обработки этого запроса приложение "звонит" POST запросом
#    в Telegram API.

# Polling-вариант:
# 1. Запускаем цикл и постоянно опрашиваем API Telegram
# Пример: 
#  https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update, context):
    """Send a message when the command /start is issued."""
    msg = ("Привет, я чатбот Финэка МГИМО! " 
           "Я появился на свет 2 мая 2020 года. "
           "Я только учусь общаться с вами.")
    update.message.reply_text(msg)


def help(update, context):
    """Send a message when the command /help is issued."""
    msg = ("По команде /help я буду рассказывать "
           "как со мной взаимодействовать.")
    update.message.reply_text(msg)


def echo(update, context):
    """Echo the user message."""
    msg = (
f"""Я услышал от вас:
- {update.message.text}
Пока я не знаю, что делать с этой информацией. (("""
)
    update.message.reply_text(msg)

# На локальной машине - запишем API_TOKEN и PROXY_URL
# в системные переменные из 'config.env'.
# На удаленной машине это будет сделано через меню настроек.
load_dotenv('config.env')      
API_TOKEN = os.getenv("API_TOKEN")
PROXY_URL = os.getenv("PROXY_URL")

def app(token: str = API_TOKEN, proxy_url: str=PROXY_URL):
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, 
                      request_kwargs={'proxy_url': proxy_url},
                      use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # log all errors
    dp.add_error_handler(error)    

    # on different commands - answer in Telegram
    for name, func in [("start", start), ("help", help)]:
       dp.add_handler(CommandHandler(name, func))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':        
    app()