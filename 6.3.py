# 6.3 Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише 
# зімнні типу стрінг, які присутні в lst1. Данні в листі можуть бути будь якими
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []

for item in lst1:
    if type(item) == str:
        lst2.append(item)

print(lst2)