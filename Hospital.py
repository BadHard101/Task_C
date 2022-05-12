"""
Создать класс Hospital. Поля: название больницы, адрес, список врачей (список экземпляров класса Doctor),
    список медсестер (список экземпляров класса Nurse). Определить конструктор. Переопределить метод преобразования
    в строку для печати всей информации о больнице (с использованием переопределения в классах Doctor и Nurse).
    Переопределить методы получения количества врачей функцией len, получения врача по индексу, изменения
    по индексу, удаления по индексу (пусть номера врачей считаются с 1, а индекс 0 – список всех медсестер).
    Переопределить операции + и - для добавления или удаления врача.
"""

from Doctor import Doctor
from Nurse import Nurse

class Hospital:
    def __init__(self, arg_name, arg_address):
        self.name = arg_name
        self.address = arg_address
        self.doctor_list = []
        self.nurse_list = []

    def __len__(self):
        return len(self.doctor_list)

    def __getitem__(self, arg_index):
        try:
            if (arg_index==0):
                print("List of Nurses:")
                for i in range(len(self.nurse_list)):
                    print(self.nurse_list[i])
            else:
                print(self.doctor_list[arg_index-1])
        except:
            print("Error: Incorrect index. Try other!")

    def __delitem__(self, arg_index):
        try:
            if (arg_index==0):
                self.nurse_list = []
                print("Nurse's list was cleared successfully")
            else:
                print(self.doctor_list.pop(arg_index - 1))
                print("Doctor was deleted successfully")
        except:
            print("Error: Incorrect index. Try other!")

    def __setitem__(self, arg_index, new_doctor):
        try:
            if (arg_index==0):
                print("You cannot change the nurse list")
            else:
                self.doctor_list[arg_index - 1] = new_doctor
                print("Doctor was changed successfully")
        except:
            print("Error: Incorrect index. Try other!")

    def __sub__(self, doctor):
        try:
            self.doctor_list.remove(doctor)
        except:
            print("Such doctor doesn't exist. Try other!")
        finally:
            return self.doctor_list

    def __add__(self, doctor):
        self.doctor_list.append(doctor)
        return self.doctor_list

    def __str__(self):
        s = f'Name of Hospital: {self.name}\nAddress: {self.address}\n\nList of doctors:\n'
        for i in range(len(self.doctor_list)):
            s += str(self.doctor_list[i]) + "\n"
        s += "List of Nurses:\n"
        for i in range(len(self.nurse_list)):
            s += str(self.nurse_list[i]) + "\n"
        return s

    """
    Добавить функцию создания txt-файла и записи всей информации в него 
    (в том числе пациентов врачей и графика работы медсестер).
    """
    def file(self, address):
        f = open(address, "w")

        s = f'Name of Hospital: {self.name}\nAddress: {self.address}\n\n\nList of doctors:\n\n'
        for i in range(len(self.doctor_list)):
            s += str(self.doctor_list[i]) + "\n"
            s = s + str(self.doctor_list[i].print_patient_list()) + "\n\n"

        s += "\nList of Nurses:\n\n"
        for i in range(len(self.nurse_list)):
            s += str(self.nurse_list[i]) + "\n" + str(self.nurse_list[i].get_schedule()) + "\n\n"

        f.writelines(s)
