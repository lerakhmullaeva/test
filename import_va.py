#  1 - імпорт модуля
import logging          # built-in
import os               # built-in
import json             # built-in
import requests         # installed
import math             # built-in

# 2 - імпорт чогось конкретного
from math import sqrt
from json import dumps
from os import getenv
from logging import getLogger
from requests import get

# 3 - "імпорт сам не знаю чого" (динамічний/умовний)
try:
    import ujson as fast_json
except ImportError:
    import json as fast_json

# 4 - імпорт через псевдонім (alias)
import logging as log
import requests as req
from datetime import datetime as dt
from math import sqrt as square_root
from json import dumps as json_dumps


# Ніяких побічних викликів (print, HTTP, логінг) на рівні модуля —
# лише під час запуску як скрипта.
if __name__ == "__main__":
    # Налаштування логера один раз (щоб уникнути дублювання handlers при повторних викликах)
    root = logging.getLogger()
    if not root.handlers:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    logger = logging.getLogger("imports_demo")

    # Демонстрація використання (виконується лише при прямому запуску)
    logger.info("Alias logging works (demo)")

    # HTTP-запит — демонстрація (можна видалити, якщо у вас немає мережі)
    try:
        response = req.get("https://example.com", timeout=5)
        print("HTTP status (example.com):", response.status_code)
    except Exception as e:
        print("HTTP demo failed (this is okay in some environments):", e)

    print("now:", dt.now())
    print("square_root(49):", square_root(49))
    print("json_dumps:", json_dumps({"alias": True}))
    print("fast_json.dumps (fallback ok):", fast_json.dumps({"fallback": True}))
    print("PATH env (getenv):", getenv("PATH")[:80], "...")  # короткий зріз для читабельности
    print("sqrt(16):", sqrt(16))
