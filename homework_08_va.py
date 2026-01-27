# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік", та "середній бал". 
# Створіть об'єкт цього класу, представляючи студента. 
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента. 
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, avg_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_grade = avg_grade


    def greet(self):
        return f"Student name is {self.name}, surname is {self.surname}. {self.name}'s age is {self.age} and his grade is {self.avg_grade}"
    

    def set_grade(self, new_grade = 0):
        self.avg_grade = new_grade
        return(f"Average grade was changed to {self.avg_grade}")
        
        
student_1 = Student(name = "Ivan", surname = 'Franko', age = 35, avg_grade = 82)

# print(student_1.greet())
print(student_1.greet())
print(student_1.set_grade(90))