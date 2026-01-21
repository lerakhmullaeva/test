# 1. Візьміть два файли з теки, порівняйте на наявність дублікатів і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv


from pathlib import Path   # для роботи зі шляхами
import csv                 # для читання/запису CSV

SECOND_NAME = "Akhmullaieva"

# Папка, де лежить цей файл (1.py / task_csv.py)
base_dir = Path(__file__).resolve().parent

# Знаходимо всі CSV у цій папці, крім файлів, які починаються на result_
csv_files = [f for f in base_dir.glob("*.csv") if not f.name.startswith("result_")]

# Переконаємось, що є хоча б два csv-файли
if len(csv_files) < 2:
    raise RuntimeError(f"У папці {base_dir} має бути як мінімум 2 csv-файли")

# Беремо перші два файли зі списку
file1 = csv_files[0]
file2 = csv_files[1]

# Шлях до файлу з результатом
output_file = base_dir / f"result_{SECOND_NAME}.csv"

# --- ЧИТАЄМО ПЕРШИЙ CSV ---

with file1.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader, [])        # перший рядок як заголовок
    rows1 = list(reader)             # всі інші рядки

# --- ЧИТАЄМО ДРУГИЙ CSV (ігноруємо його header, беремо тільки дані) ---

with file2.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    _ = next(reader, [])             # пропускаємо заголовок
    rows2 = list(reader)

# --- ОБ'ЄДНУЄМО РЯДКИ ТА ПРИБИРАЄМО ДУБЛІКАТИ ---

all_rows = rows1 + rows2             # всі рядки з обох файлів

# set залишає тільки унікальні елементи, тому дублікати "зникнуть"
unique_rows = []
seen = set()

for row in all_rows:
    key = tuple(row)                 # list не можна класти в set, тому робимо tuple
    if key not in seen:
        seen.add(key)
        unique_rows.append(row)

# --- ЗАПИСУЄМО РЕЗУЛЬТАТ У result_<second_name>.csv ---

with output_file.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    if header:
        writer.writerow(header)      # пишемо заголовок один раз
    writer.writerows(unique_rows)    # усі унікальні рядки

print("Знайдені CSV:", [p.name for p in csv_files])
print("Вихідний файл:", output_file.name)
print("К-сть рядків до/після:", len(all_rows), "->", len(unique_rows))
