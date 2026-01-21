# 3. Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming 
# результат виведіть у консоль через логер на рівні інфо

from pathlib import Path                          # Щоб будувати шлях до XML-файлу
import logging                                   # Щоб виводити результат через logger на рівні INFO
import xml.etree.ElementTree as ET               # Щоб читати і шукати дані в XML

# 1) Створюємо логер для виводу в консоль
logger = logging.getLogger("xml_search")         # Створюємо/отримуємо логер з ім'ям
logger.setLevel(logging.INFO)                    # Кажемо логеру пропускати INFO і вище

# 2) Створюємо handler, який виводить логи у консоль
console_handler = logging.StreamHandler()        # Handler для консолі
console_handler.setLevel(logging.INFO)           # Виводимо тільки INFO і вище

# 3) Налаштовуємо формат повідомлення в консолі
formatter = logging.Formatter("%(levelname)s | %(message)s")  # Формат: рівень | текст
console_handler.setFormatter(formatter)          # Призначаємо формат handler'у

# 4) Підключаємо handler до логера (інакше логер не буде нічого виводити)
logger.addHandler(console_handler)

# 5) Функція: шукає group за number і повертає timingExbytes/incoming
def find_incoming_by_group_number(xml_path: Path, group_number: str) -> str:
    # 6) Читаємо XML з файлу в структуру (дерево)
    tree = ET.parse(xml_path)

    # 7) Беремо кореневий елемент XML, від якого починається пошук
    root = tree.getroot()

    # 8) Проходимо по всіх тегах <group> у файлі
    for group in root.findall(".//group"):
        # 9) Знаходимо всередині group тег <number>
        number_el = group.find("number")

        # 10) Якщо тега <number> нема — пропускаємо цей group
        if number_el is None:
            continue

        # 11) Якщо number співпадає з тим, що ми шукаємо — знаходимо incoming
        if (number_el.text or "").strip() == str(group_number):
            incoming_el = group.find(".//incoming")
            if incoming_el is None:
                print("Для group number", group_number, "немає incoming. Дочірні теги group:", [c.tag for c in group])
                return ""

            return (incoming_el.text or "").strip()

    # 14) Якщо group з таким number не знайдено — повертаємо порожній рядок
    return ""

def main():
    # 15) Знаходимо папку, де лежить цей скрипт, щоб стабільно будувати шлях до XML
    base_dir = Path(__file__).resolve().parent

    # 16) Будуємо шлях до XML файлу згідно умови задачі
    xml_path = base_dir / "groups.xml"

    # 17) Вказуємо group number, який хочемо знайти (можеш змінити на свій)
    number_to_search = "2"

    # 18) Викликаємо функцію пошуку і отримуємо incoming
    incoming_value = find_incoming_by_group_number(xml_path, number_to_search)

    # 19) Виводимо результат через logger на рівні INFO (як вимагає умова задачі)
    logger.info("group/number=%s -> timingExbytes/incoming=%s", number_to_search, incoming_value)

if __name__ == "__main__":
    main()