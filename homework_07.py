# # task 1
# """ Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити."""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# # task 2
# """  Написати функцію, яка обчислює суму двох чисел."""
def add_numbers(a, b):
 return a + b
result = add_numbers(10,4)
print(result)

# # task 3
# """  Написати функцію, яка розрахує середнє арифметичне списку чисел."""
def average(numbers):
    if len(numbers) == 0:   
        return 0
    return sum(numbers) / len(numbers)
nums = [0, 10, 15]
result = average(nums)
print("Середнє арифметичне:", result)

# # task 4
# """  Написати функцію, яка приймає рядок та повертає його у зворотному порядку."""
def reverse_string(text):
    return text[::-1]
print(reverse_string("Ukraine"))

# # task 5
# """  Написати функцію, яка приймає список слів та повертає найдовше слово у списку."""
def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
lst = ["Python", "Ukraine", "Varenyky"]
print(longest_word(lst))

# # task 6
# """  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок не є підрядком першого рядка."""
def find_substring(str1, str2):
#      # Якщо другий рядок довший за перший — він точно не може бути підрядком
    if len(str2) > len(str1):
        return -1
#     # Проходимо по кожній можливій позиції в str1
    for i in range(len(str1) - len(str2) + 1):
#         # Беремо фрагмент str1 тієї ж довжини, що й str2
        if str1[i : i + len(str2)] == str2:
            return i  # якщо збіг — повертаємо індекс

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# # task 7 - 10
# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним. """

# task 7
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

def dishes(big_pizza, medium_pizza, juice, cake, water):
 return (big_pizza * 4) + (medium_pizza * 2) + (juice * 4) + cake + (water * 3)
total_sum = dishes(274, 218, 35, 350, 21)
print(total_sum)

# task 8
# max_photo_per_page = 8
# total_photos = 232
# pages_amount = (total_photos + max_photo_per_page - 1) // max_photo_per_page
# print(pages_amount)

def photobook(total_photos, max_photo_per_page):
 return (total_photos + max_photo_per_page - 1) // max_photo_per_page
pages_amount = photobook(232, 8)
print(pages_amount)


# task 9
# boys = 24
# girls = boys // 2
# sick_boy = 1
# absent_girl = 2
# # theater_team = boys + girls
# todays_general_amount = (boys - sick_boy) + (girls - absent_girl)
# print("Сьогодні в театральний гурток прийшло", todays_general_amount, ", з них", girls - 2, "дівчат та", boys - 1, "хлопців.")

def garden(boys, sick_boys, absent_girl):
    girls = boys // 2
    return (boys - sick_boys) + (girls - absent_girl)
total = garden(24,1,2)
print(total)

# task 10
# be4_lunch_t = 5
# after_lunch_t = be4_lunch_t - 10
# afternoon_t = after_lunch_t + 4
# print("Afternoon temaperature is", afternoon_t)

def temperature(be4_lunch_t):
    after_lunch_t = be4_lunch_t - 10
    afternoon_t = after_lunch_t + 4
    return afternoon_t
end_day_t = temperature(5)
print(end_day_t)

# def say_hello(name):
    print(f"привіт, {name}")  #exersice for myself

# say_hello("Валерія")