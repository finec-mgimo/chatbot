# chatbot

A simple chatbot example - just \start and \help commands and and relaying text you just said.

You can expect to communicate with a bot like:

```
/start
FinecJuniorBot: Привет, я младший чатбот Финэка МГИМО! Я появился на свет 2 мая 2020 года. Я только учусь общаться с вами.

/help
FinecJuniorBot: По команде /help я буду рассказывать как со мной взаимодействовать.

Do you use proxy?
FinecJuniorBot: Я услышал от вас:
- Do you use proxy?
Пока я не знаю, что делать с этой информацией. ((
```

## How to reproduce

1. Obtain an individual API token from Telegram's `@FatherBot`

2. Clone this repo, go to repo directory:

```
git clone https://github.com/finec-mgimo/chatbot.git
cd chatbot
```

3. Create text file `config.txt` with following content

```
API_TOKEN=<your token from @BotFather here>
```

4. Make sure depenencies are installed:

```
pip install -U -r requirements.txt
```
(or even better use virtual environment)

5. Start the bot:

```
python application.py
```

6. Talk to your bot in Telegram:

```
/start
/help
Type any ecent text you like!
```
