# Примечание: задачи 1-3 должны иметь следующую сигнатуру def function_name(callback, sequence).
# Аннотации дописать самим. Функции должны уметь работать с целыми числами, числами с плавающей
# точкой и строками в качестве элементов последовательностей. В качестве последовательностей могут
# быть переданы списки, кортэжи, словари. Буду проверять с помощью майпай аннотации.
from typing import Callable, Sequence



def myFilter(callback: Callable, sequence: Sequence) -> Sequence:
    """
        Returns the sequence with only those elements, where function result
        is True
    """
    filteredList = list()

    for i in sequence:
        if callback(i) is True:
            filteredList.append(i)
    return filteredList


def f(x):
    return x > 55

a = [50, 60, 500, 100]
# f = lambda x: x > 100
print(list(filter(f, a)))