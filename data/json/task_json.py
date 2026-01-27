# 2. Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. Результат для невалідного файлу виведіть через логер на рівні
# еррор у файл json_<your_second_name>.log

from pathlib import Path       # для роботи зі шляхами
import json                    # для читання/парсингу JSON
import logging                 # для логування помилок у файл

SECOND_NAME = "Akhmullaieva"

# Папка, де лежить цей файл (1.py / task_json.py)
base_dir = Path(__file__).resolve().parent

# Лог-файл, куди будемо писати помилки JSON
log_file = base_dir / f"json_{SECOND_NAME}.log"

# --- НАЛАШТОВУЄМО ЛОГЕР, ЯКИЙ ПИШЕ ERROR У ФАЙЛ ---

logging.basicConfig(
    filename=log_file,                  # куди писати логи
    level=logging.ERROR,                # логувати тільки ERROR і вище
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# --- ЗНАХОДИМО УСІ JSON-ФАЙЛИ У ПАПЦІ ---

json_files = list(base_dir.glob("*.json"))  # усі *.json поруч зі скриптом

print("JSON файли для перевірки:", [p.name for p in json_files])

# --- ПЕРЕВІРЯЄМО КОЖЕН ФАЙЛ НА ВАЛІДНІСТЬ ---

for path in json_files:
    try:
        with path.open("r", encoding="utf-8") as f:
            json.load(f)   # якщо JSON кривий – тут буде помилка JSONDecodeError

    except json.JSONDecodeError as e:
        # Невалідний JSON – логимо як ERROR у файл
        logging.error("Invalid JSON file: %s | Error: %s", path.name, e)

    except Exception as e:
        # Будь-яка інша помилка (наприклад, немає доступу до файлу)
        logging.error("Cannot process file: %s | Error: %s", path.name, e)

print("Перевірка завершена. Лог помилок (якщо були):", log_file.name)
