import os

import telebot
from dotenv import load_dotenv


# Мы записали секретное значение в системную переменную TOKEN
# для локальной разработки через файл "token.env".
# На удаленной машине это будет сделано через меню настроек.
load_dotenv('token.env')

API_TOKEN = os.getenv("TOKEN")
assert len(API_TOKEN) == 46


# Polling-вариант:
# 

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. 
Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()


# ERROR: нужен прокси для общения с 'api.telegram.org'
# ConnectTimeout: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot1051955622:AAEtHn_rQFsA7r_fp0W-7XRiAyd7vsyqkic/getUpdates?offset=1&timeout=20 (Caused by ConnectTimeoutError(<urllib3.connection.VerifiedHTTPSConnection object at 0x0000024E3B6951D0>, 'Connection to api.telegram.org timed out. (connect timeout=3.5)'))



# Webhook-вариант:
#
# 1. приложение на Flask должно обрабтывать на входе запрос POST от Telegram 
#    на своем endpoint'е
# 2. по результатам обработки этого запроса приложение "звонит" POST запросом
#    в Telegram API.
# 3. минмиальный сценарий: на каждый чих пользователя бот говорит "Я что-то слышу!"
# 4. мы можем хранить все, что наговорили роботу для последующего анализа
#

#
# Ограничения:
# 
# - все делается последовательно, нет аснихронности / балансировщика
#
 