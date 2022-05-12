"""
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
"""
class Person:
    def __init__(self, arg_name, arg_surname, arg_age):
        self.name = arg_name
        self.surname = arg_surname
        self.age = arg_age