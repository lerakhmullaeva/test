# 6.1
def my_string(text):
    if len(text) > 10:
        return (True)
    else: 
        return (False)
    
# 6.2
def word(text):
    return "h" in text.lower()

# 6.3
def filter_strings(data):
     # створюємо порожній список
    # сюди будемо складати тільки рядки (str)
    result = []
    # проходимося по кожному елементу зі списку data
    for item in data:
     # перевіряємо: чи є поточний елемент рядком (тип str)
        if isinstance(item, str):
        # якщо так — додаємо цей елемент у список result
            result.append(item)
            # після завершення циклу повертаємо новий список,
            # який містить тільки рядки
    return result

# lesson13
# @pytest.mark.smoke
def add(a, b):
    return a + b

# @pytest.mark.parametrize
def param(a, b):
    return a + b

# @pytest.fixture
def adding(a, b):
    return a + b