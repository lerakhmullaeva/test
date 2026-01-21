# 6.4 Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
list = [1, 5, 6, 4, 8, 0, 22, 26, 3, 5, 43, 44, 2]

result = 0
for num in list:
    if num % 2 == 0:
        result += num

print(result)
