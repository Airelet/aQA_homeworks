# Создайте класс с описанием любой компании. К примеру тошиба или глобал лоджик. Company.
# Хочу видеть чистый код. Ожидажю увидеть чистый код с аннотациями. Пока что без связей первого класса со вторым.
# Во всех методах ожидаю увидеть докстринги с вменяемым описанием.
from datetime import MINYEAR, MAXYEAR, datetime

from dateutil.relativedelta import relativedelta


class Company:
    def __init__(self,
                 name: str,
                 employees: int = None,
                 year_founded: int = None,
                 industry: str = None,
                 headquarters: str = None,
                 market_value: int = None,
                 parent_company: str = None,
                 child_company: str = None):
        self.__name = name
        self.__employees = employees
        self.__year_founded = year_founded
        self.__industry = industry
        self.__headquarters = headquarters
        self.__market_value = market_value
        self.__parent_company = parent_company
        self.__child_company = child_company

    @property
    def name(self):
        return self.__name

    @property
    def employees(self):
        return self.__employees

    @property
    def year_founded(self):
        return self.__year_founded

    @property
    def industry(self):
        return self.__industry

    @property
    def headquarters(self):
        return self.__headquarters

    @property
    def market_value(self):
        return self.__market_value

    @property
    def parent(self):
        return self.__parent_company

    @property
    def child(self):
        return self.__child_company

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @employees.setter
    def employees(self, updated_employees):
        self.__employees = updated_employees

    @year_founded.setter
    def year_founded(self, updated_founded):
        if MINYEAR <= updated_founded <= MAXYEAR:
            self.__year_founded = updated_founded
        else:
            print("Your year is out of boundaries, try again")

    @industry.setter
    def industry(self, new_industry):
        self.__industry = new_industry

    @headquarters.setter
    def headquarters(self, new_headquarters):
        self.__headquarters = new_headquarters

    @market_value.setter
    def market_value(self, new_market_value):
        self.__market_value = new_market_value

    def to_datetime(self):
        return datetime.strptime(str(self.year_founded), '%Y')

    @classmethod
    def company_age(cls, company):
        return relativedelta(datetime.now(), company.to_datetime()).years

    @staticmethod
    def valid_german_vat(vat_id):
        return type(vat_id) is str and len(vat_id) == 12 and str(vat_id).startswith("DE")


if __name__ == '__main__':
    abc = Company("Abc", 15)

    print(abc.name)
    abc.name = "Cool name"
    print(abc.name)
    print(abc.employees)
    abc.year_founded = 176
    print(abc.year_founded, "\n")
    abc.year_founded = 2020
    print(abc.year_founded)
    print(Company.company_age(abc))
    print(Company.valid_german_vat("DE1234567890"))
    
