# 2. Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. Результат для невалідного файлу виведіть через логер на рівні
# еррор у файл json_<your_second_name>.log
# 3. Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming 
# результат виведіть у консоль через логер на рівні інфо



from pathlib import Path                 # Щоб зручно працювати зі шляхами до папок/файлів
import json                              # Щоб пробувати читати/парсити JSON
import logging                           # Щоб писати помилки в лог-файл (а не print)

SECOND_NAME = "Akhmullaieva"             # Твоє прізвище для назви лог-файлу

# 1) Визначаємо папку, де лежить цей скрипт (щоб будувати шляхи стабільно)
base_dir = Path(__file__).resolve().parent

# 2) Вказуємо шлях до папки, де лежать JSON-файли за умовою задачі
json_dir = base_dir

# 3) Формуємо шлях до лог-файлу, куди будемо писати ERROR
log_file = base_dir / "json_Akhmullaieva.log"

# 4) Створюємо логер (іменований) — це “об’єкт для логування”
logger = logging.getLogger("json_validator")

# 5) Встановлюємо рівень логера (він має пропускати ERROR)
logger.setLevel(logging.ERROR)

# 6) Створюємо handler, який пише логи у файл (саме він фізично записує в .log)
file_handler = logging.FileHandler(log_file, encoding="utf-8")

# 7) Кажемо handler’у писати тільки ERROR і вище
file_handler.setLevel(logging.ERROR)

# 8) Задаємо формат логів (час + рівень + повідомлення) — щоб було як у справжніх логах
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
file_handler.setFormatter(formatter)

# 9) Підключаємо handler до логера (без цього логер “нікуди” не пише)
logger.addHandler(file_handler)

# 10) Знаходимо всі файли .json у потрібній папці (задача просить перевірити всі)
json_files = list(json_dir.glob("*.json"))

# 11) Проходимо по кожному json файлу і пробуємо його прочитати як JSON
for file_path in json_files:
    try:
        # 12) Відкриваємо файл для читання тексту (utf-8 — стандарт для json)
        with file_path.open("r", encoding="utf-8") as f:
            # 13) Пробуємо розпарсити JSON: якщо він невалідний — буде exception
            json.load(f)

    except json.JSONDecodeError as e:
        # 14) Якщо JSON невалідний — пишемо ERROR у лог-файл, як вимагає умова
        logger.error("Invalid JSON file: %s | Error: %s", file_path.name, e)

    except Exception as e:
        # 15) Якщо сталася інша помилка (наприклад файл не читається) — теж логимо як ERROR
        logger.error("Cannot process file: %s | Error: %s", file_path.name, e)
