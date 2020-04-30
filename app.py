import os
from dotenv import load_dotenv

# Записали секретное значение в системную переменную TOKEN
# для локальной разработки через файл "token.env".
# На удаленной машине это будет сделано через меню настроек.
load_dotenv()

TOKEN = os.getenv("TOKEN")
assert len(TOKEN) == 46
