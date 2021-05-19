# chatbot

A simple chatbot example for MGIMO Finec.

## How to reproduce

1. Obtain an individual API token from Telegram's `@FatherBot`

2. Clone this repo, go to repo directory:

```
git clone https://github.com/finec-mgimo/chatbot.git
cd chatbot
```

3. Create text file `config.env` with following content

```
API_TOKEN=<your token here>
PROXY_URL=socks5h://163.172.152.192:1080
```

4. Make sure depenencies are installed:

```
pip install -r requirements.txt
```

5. Start the bot:

```
python application.py
```

6. Talk to your bot in Telegram:

```
/start
/help
Произвольный текст
```
