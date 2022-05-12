"""Создать производный от Person класс Nurse. Новые поля: номер удостоверения, отделение работы, график работы
(словарь вида день недели: часы работы). Определить конструктор, с вызовом родительского конструктора.
Определить функции изменения отделения, добавления, удаления и изменения графика работы. Переопределить
метод преобразования в строку для печати основной информации (ФИ, возраст, номер удостоверения, отделение).
"""

from Person import Person

class Nurse(Person):
    def __init__(self, arg_name, arg_surname, arg_age, arg_id, arg_department):
        super().__init__(arg_name, arg_surname, arg_age)
        self.id = arg_id
        self.department = arg_department
        self.schedule = {}

    def update_department(self, new_department):
        self.department = new_department

    def update_schedule_day(self, day, hours):
        self.schedule[day] = hours

    def del_schedule_day(self):
        print("Enter the day, you want to delete: ")
        del_day = str(input())
        self.schedule.pop(del_day)

    def get_schedule(self):
        s = ""
        if len(self.schedule) == 0:
            s = f"Schedule of {self.surname} {self.name} is empty now"
        else:
            s = f"Schedule of Nurse ({self.surname} {self.name}) now:\n"
            for day in self.schedule:
                s += f"{day}: {self.schedule[day]}\n"
        return s

    def del_patient(self, arg_id_patient):
        self.patient_list.pop(arg_id_patient)

    def get_info(self):
        print(self.name, self.surname, self.age)

    def __str__(self):
        s = f"Nurse's name: {self.surname} {self.name}\nAge: {self.age}   Department: {self.department}   Id: {self.id}"
        return s
