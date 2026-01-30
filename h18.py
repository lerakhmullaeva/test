# ГЕНЕРАТОРИ
# 1. Напишіть генератор, який повертає послідовнііість парних чисел від 0 до N.
def even_numbers_up_to(n: int):
    """Yield парні числа від 0 до n включно."""
    for x in range(0, n + 1):
        if x % 2 == 0:
            yield x

print(list(even_numbers_up_to(10)))
# [0, 2, 4, 6, 8, 10]

# def ... — звичайна функція, але з yield вона стає генератором.
# range(0, n + 1) — щоб включити n (бо range не включає праву межу).
# x % 2 == 0 — перевірка парності.
# yield x — повертає одне значення і “заморожує” стан, щоб продовжити з того місця наступного разу.

# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_up_to(n: int):
    """Yield числа Фібоначчі, поки вони <= n."""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci_up_to(30)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21]

# Поки a <= n — віддаємо a.
# Оновлення a, b = b, a + b:
# нове a стає попереднім b
# нове b стає сумою попередніх a+b

# ІТЕРАТОРИ
# 1. Реалізуй ітератор для зворотнього виведення елементів списку.
from typing import Any, List

class ReverseListIterator:
    def __init__(self, data: List[Any]):
        self.data = data
        self.index = len(data)  # стартуємо "після" останнього

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
    
items = [10, 20, 30]
it = ReverseListIterator(items)

for x in it:
    print(x)

# 2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenRangeIterator:
    def __init__(self, n: int):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            value = self.current
            self.current += 1
            if value % 2 == 0:
                return value
        raise StopIteration
    
print(list(EvenRangeIterator(11)))
# [0, 2, 4, 6, 8, 10]
    
# Ми йдемо від 0 вгору.
# Крутимо while, поки не знайдемо парне — тоді return.
# Коли current > n — завершуємо StopIteration.

# ДЕКОРАТОРИ
# Декоратор — це функція, яка бере іншу функцію, і повертає НОВУ функцію з додатковою поведінкою
# 1. Напишіть декоратор, який логує аргументи та результати виконаної функції.
from functools import wraps
from typing import Callable, Any

def log_call(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"[LOG] Calling {func.__name__} args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result!r}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

add(2, 5)

# *args, **kwargs — щоб декоратор працював з будь-якою функцією.
# @wraps(func) — зберігає ім’я функції, докстрінг, корисно для репортів/алюрів/дебагу.
# result!r — показує “repr”, часто інформативніше для QA.

# 2. Створіть декоратор, який перехоплює та обробляє винятки, які виконають в ході виконання функції.
from functools import wraps
from typing import Callable, Any

def handle_exceptions(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any: # Щоб працювало з будь-якими аргументами.
        try:
            return func(*args, **kwargs)
        except Exception as e: # Exception — базовий клас майже всіх помилок. e — конкретна помилка (ZeroDivisionError, ValueError, тощо)
            print(f"[ERROR] {func.__name__} failed with {type(e).__name__}: {e}")
            # для QA краще не ковтати ексепшн:
            raise # raise без аргументів - повторно кидає ту саму помилку
    return wrapper

@handle_exceptions
def divide(a, b):
    return a/b

divide(10, 0)
# [ERROR] divide failed with ZeroDivisionError: division by zero
# потім впаде з ZeroDivisionError

