# # alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# # # task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# alice_in_wonderland = (
#     '"Would you tell me, please, which way I ought to go from here?"\n'
#     '"That depends a good deal on where you want to get to," said the Cat.\n'
#     '"I don\'t much care where ——" said Alice.\n'
#     '"Then it doesn\'t matter which way you go," said the Cat.\n'
#     '"—— so long as I get somewhere," Alice added as an explanation.\n'
#     '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# )

# # # task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# for char in alice_in_wonderland:
#     if char == "'":
#         print(char)

# # # task 03 == Виведіть змінну alice_in_wonderland на друк
# print(alice_in_wonderland)

# """
#     # Задачі 04 -10:
#     # Переведіть задачі з книги "Математика, 5 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в п'ятому класі
# """
# # task 04
# """
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азовське моря разом?
# P_B_sea = 436402
# P_A_sea = 37800
# seas_together = P_B_sea + P_A_sea
# print(seas_together)

# # task 05
# """
# Мережа супермаркетів має 3 склади, де всього розміщено 375 291 товар. На першому та другому складах перебуває 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.
# total = 375291
# s1_s2 = 250449
# s2_s3 = 222950
# s1 = (total - s2_s3)
# s3 = (total - s1_s2)
# s2 = (s1 - s3)
# print("Всього на першому складі:", s1, ", на другому складі:", s2, ", і на третьому складі", s3)

# # task 06
# """
# Михайло разом з батьками вирішили купити комп’ютер, скориставшись послугою «Оплата частинами». Відомо, що сплачувати необхідно буде півтора року по 1179 грн/місяць. 
# Обчисліть вартість комп’ютера.
# one_month_payment = 1179
# months_in_one_year = 12
# computer = one_month_payment * (months_in_one_year + (months_in_one_year / 2))
# print(computer)


# # task 07
# """
# Знайди остачу від діленя чисел:
# a = 8019 % 8     
# d = 7248 % 6
# b = 9907 % 9    
# e = 7128 % 5
# c = 2789 % 5   
# f = 19224 % 9
# print(a, d, b, e, c, f)


# # task 08
# """
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн

# big_pizza = 274
# medium_pizza = 218
# juice = 35
# cake = 350
# water = 21
# big_pizza_sum = big_pizza * 4
# medium_pizza_sum = medium_pizza * 2
# juice_sum = juice * 4
# cake_sum = cake * 1
# water_sum = water * 3
# total_sum = big_pizza_sum + medium_pizza_sum + juice_sum + cake_sum + water_sum
# print(total_sum)
"""


# # task 09
# """
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
# """

# max_photo_per_page = 8
# total_photos = 232
# pages_amount = total_photos // max_photo_per_page
# print(pages_amount)


# # task 10
# """
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
distance = 1600
liter_per_100_km = 9
oil_tank = 48
required_liters = (distance / 100) * liter_per_100_km
print (required_liters)
stops_amount = required_liters / oil_tank
print(stops_amount)