# Создайте класс с описанием работника. Любого работника. Employee.
from dataclasses import dataclass
from datetime import datetime
from dateutil.relativedelta import relativedelta


@dataclass(frozen=False)
class Employee:
    __first_name: str
    __second_name: str
    __position: str
    __level: int
    __birthday: str
    __salary: int
    __gender: chr

    @property
    def first_name(self):
        return self.__first_name

    @property
    def second_name(self):
        return self.__second_name

    @property
    def position(self):
        return self.__position

    @property
    def level(self):
        return self.__level

    @property
    def birthday(self):
        return self.__birthday

    @property
    def salary(self):
        return self.__salary

    @property
    def gender(self):
        return self.__gender

    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @second_name.setter
    def second_name(self, second_name: str):
        self.__second_name = second_name

    @position.setter
    def position(self, position: str):
        self.__position = position

    @level.setter
    def level(self, level: int):
        self.__level = level

    @birthday.setter
    def birthday(self, birthday: str):
        self.__birthday = birthday

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @gender.setter
    def gender(self, gender: chr):
        self.__gender = gender

    def to_datetime(self):
        return datetime.strptime(self.birthday, '%d.%m.%Y')

    @classmethod
    def age(cls, employee):
        return relativedelta(datetime.now(), employee.to_datetime()).years

    @classmethod
    def birthday_date_and_month(cls, employee):
        return employee.to_datetime().strftime('%d %b')

    def __str__(self):
        return (f"Name: {self.first_name} {self.second_name}\n"
                f"Age: {self.age(self)}\t\tBirthday: {self.birthday_date_and_month(self)}\n"
                f"Position: {self.level} {self.position}")

    @classmethod
    def print_info(cls, employee):
        print(cls.__str__(employee))


if __name__ == '__main__':
    jojo = Employee("Jojo", "Mo", "Office Manager", "8", "20.04.2000", "800", 'f')
    print(jojo.first_name)
    clara = Employee("Clara", "Jin", "QA", "6", "16.09.1991", "1500", 'f')
    alex = Employee("Alex", "Dou", "CEO", "1", "08.05.1988", "12000", 'm')
    patrick = Employee("Patrick", "Wilson", "Designer", "7", "09.10.2002", "1000", 'm')
    patrick.first_name = "Patrisha"
    patrick.gender = "d"
    print(Employee.age(alex), '\n')
    print(clara, '\n')
    Employee.print_info(patrick)
