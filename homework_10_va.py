# Завдання 1
# Створіть клас Employee, який має атрибути name та salary. 
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee. 
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.

# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. 
# Цей клас представляє керівника з команди розробників. 
# Клас TeamLead повинен мати всі атрибути як Manager (імʼя, зарплата, відділ), 
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
# 
# 
# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. 
# Властивості по типу "довжина сторони" Й т.д. повинні бути приватними, та ініціалізуватись через конструктор. 
# Створіть декілька різних об'єктів фігур, та у циклі порахуйте та виведіть в консоль площу та перемитр кожної.

class Employee:
    def __init__(self, name = "", salary = 0):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name = "", salary = 0, department = ""):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name = "", salary = 0, programming_language = ""):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Employee):
    def __init__(self, name = "", salary = 0, department = "", team_size = 0):
        super().__init__(name, salary)
        self.department = department
        self.team_size = team_size

teamlead = TeamLead("Valeriia", 20.50, "QA", 75)
print(teamlead.name)
print(teamlead.salary)
print(teamlead.team_size)
print(teamlead.department)




from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

class Square(Shape):


    def __init__(self, side):
        self.__side = side

    def square(self):
        return self.__side**2
    
    def perimetr(self):
        return 4*self.__side
    
class Circle(Shape):


    def __init__(self, radius):
        self.__radius = side

    def square(self):
        return pi*(self.__radius)**2
    
    def perimetr(self):
        return 4*pi*self.__radius