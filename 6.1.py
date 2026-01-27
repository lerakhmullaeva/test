# 6.1 Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - 
#  вивести їх в консоль True, інакше - False. Строку отримати за допомогою input()
string = input("Enter you string: ")
my_string = set(string)
if len(my_string) > 10:
    print(True)
else:
    print(False)