# # task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# # # # task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# # # # task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(10*letter)

# # task 04 == Зробіть так, щоб кількість бананів була
# # завжди в чотири рази більша, ніж яблук
apples = 2
banana = 4*apples
print(banana)

# # task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# # # task 06 == Порахуйте периметр фігури з task 05
# # # та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print(perimetery)


# """
#     # Задачі 07 -10:
#     # Переведіть задачі з книги "Математика, 2 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в другому класі
# """
# # task 07
# """
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?
# """
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
trees = apple_tree + pear_tree + plum_tree
print("Всього в саду посадили:", trees, "дерев")

# # task 08
# """
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?
# """
be4_lunch_t = 5
after_lunch_t = be4_lunch_t - 10
afternoon_t = after_lunch_t + 4
print("Afternoon temaperature is", afternoon_t)



# # task 09
# """
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?
# """
boys = 24
girls = boys // 2
sick_boy = 1
absent_girl = 2
# theater_team = boys + girls
todays_general_amount = (boys - sick_boy) + (girls - absent_girl)
print("Сьогодні в театральний гурток прийшло", todays_general_amount, ", з них", girls - 2, "дівчат та", boys - 1, "хлопців.")

# # task 10
# """
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
# """

first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
total_sum = first_book + second_book + third_book
print(total_sum)