# Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек - наприклад Timestamp
# 05:45:40, а в наступному повідомлені — Timestamp 05:45:09 (тут різниця heartbeat в 31 секунду)
# Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один потік - Кеу TSTFEED0300|7E3E|0400
# Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt
# 1. Відберіть лише строки з вказаним ключем Кеу TSTFEED0300|7E3E|0400
# 2. Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
#   - для кожного випадку де heartbeat більше 31 сек але менше 33 погувало WARNING в файл hb_test.log
#   - для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
# 3. Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.
# Обовʼязково включіть результат роботи — файл hb_test.log в PR.
# Підказка 1
# 1. Прочитайте файл по строкам, якщо забули як - зверніться до 12 лекці.
# 2. Виберіть строки з необхідним значенням:
# filtered_log = []
# if "key" in "Long log string with key":
#   filtered_log-append("long log string with key")
# Підказка 2
# 1. Пошук часу у строці можна зробити методом .find("Timestamp ") і повернути наступні 8 символів
# 2. Перетворити строку в час дозволяє метод .strptime(*10:00:00", *%H:%M:%S*)
# 3. Значення слід аналізувати парами - від поточного відняти наступне і залогувати (або не залогувати) результат

from datetime import datetime
KEY = "TSTFEED0300|7E3E|0400"

def analyze_heartbeat_log(input_file: str, output_file: str, key: str) -> None:
    filtered = []

    # 1) читаємо лог і залишаємо тільки рядки з key
    with open(input_file, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if key not in line:
                continue

            idx = line.find("Timestamp ")
            if idx == -1:
                continue

            time_str = line[idx + len("Timestamp ") : idx + len("Timestamp ") + 8]

            try:
                ts = datetime.strptime(time_str, "%H:%M:%S")
            except ValueError:
                continue

            filtered.append(ts)

    # 2) аналізуємо сусідні значення (як у підказці: "від поточного відняти наступне")
    with open(output_file, "w", encoding="utf-8") as out:
        for i in range(1, len(filtered)):
            prev_time = filtered[i - 1]
            curr_time = filtered[i]

            diff = (prev_time - curr_time).total_seconds()

            # якщо лог переходить через північ (наприклад 00:00 -> 23:59)
            if diff < 0:
                diff += 24 * 60 * 60

            # 3) логіка WARNING / ERROR
            if 31 < diff < 33:
                out.write(f"WARNING: heartbeat {diff:.0f}s at {curr_time.strftime('%H:%M:%S')}\n")
            elif diff >= 33:
                out.write(f"ERROR: heartbeat {diff:.0f}s at {curr_time.strftime('%H:%M:%S')}\n")


if __name__ == "__main__":
    analyze_heartbeat_log("hblog.txt", "hb_test.log", KEY)
    print("Done! Created hb_test.log")
