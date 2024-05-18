# Создать декоратор которые принтит в консоль имя функции которая была вызвана.
# Функция при этом должна работать как и задумывалось.
# К примеру создайте пару функции для арифметических операций суммирования и умножения.
# При вызове этих функций должен возвращаться результат операции и предварительно выводиться в консоль имя функции
# которая была вызвана.
from functools import wraps

def decorate(sign):
    def middle(func):
        @wraps(func)
        def low(nums):
            print(func.__name__)
            top = (sign * len(nums)) + (sign * 32)
            bottom = (sign * len(nums)) + (sign * 32)
            return f"{top}\n{func(nums)}\n{bottom}"
        return low
    return middle


@decorate('-')
def plus(nums):
    result = 0
    for i in nums:
        result += i
    return result


@decorate('=')
@decorate('%')
def mult(nums):
    result = 1
    for i in nums:
        result = result * i
    return result


listOfNumbers = [1, 7, 7, 20, 2]

print(plus(listOfNumbers))
print(mult(listOfNumbers))
