# 1. Візьміть два файли з теки, порівняйте на наявність дублікатів і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv


from pathlib import Path            # Імпортуємо Path, щоб зручно працювати зі шляхами до файлів/папок
import csv                          # Імпортуємо csv, щоб читати і записувати CSV-файли

SECOND_NAME = "Akhmullaieva"        # Твоє прізвище для назви вихідного файлу

# 1) Визначаємо папку, де лежить цей скрипт (1.py), щоб шукати файли поруч із ним
base_dir = Path(__file__).resolve().parent

# 2) Знаходимо у цій папці всі файли з розширенням .csv (це і є "два файли з теки")
csv_files = list(base_dir.glob("*.csv"))

# 3) Беремо перші два CSV-файли зі списку (саме їх будемо порівнювати і чистити від дублів)
file1 = csv_files[0]
file2 = csv_files[1]

# 4) Готуємо шлях до вихідного файлу, куди запишемо результат
output_file = base_dir / f"result_{SECOND_NAME}.csv"

# 5) Читаємо перший CSV: заголовок (header) і всі рядки (rows)
with file1.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)                      # Створюємо reader, який читає CSV построчно
    header = next(reader)                       # Беремо перший рядок як заголовок колонок
    rows1 = list(reader)                        # Зчитуємо всі інші рядки в список

# 6) Читаємо другий CSV: пропускаємо заголовок і беремо всі рядки (дані)
with file2.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)                      # Створюємо reader для другого файлу
    next(reader)                                # Пропускаємо перший рядок (заголовок)
    rows2 = list(reader)                        # Зчитуємо дані (рядки) в список

# 7) Об'єднуємо рядки з обох файлів в один список (тепер працюємо з усіма даними разом)
all_rows = rows1 + rows2

# 8) Прибираємо дублікати: set зберігає тільки унікальні значення, тому рядки-дублі не повторяться
unique_rows = list({tuple(row) for row in all_rows})   # tuple потрібен, бо list не можна покласти в set

# 9) Записуємо результат у файл result_<second_name>.csv: спочатку заголовок, потім унікальні рядки
with output_file.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)                      # Створюємо writer для запису CSV
    writer.writerow(header)                     # Записуємо заголовок
    writer.writerows(unique_rows)               # Записуємо всі унікальні рядки

print("Знайдені CSV:", [p.name for p in csv_files])
print("Вихідний файл:", output_file.name)
print("К-сть рядків до/після:", len(all_rows), "->", len(unique_rows))
