# Создайте функцию которая способна вернуть квадраты четных элементов для диапазона от 0 до 1000000000 включительно.
# Решение должно отрабатывать и не фризить ваш комп.
import time

start = time.time()

smallnum = 1_000_001
midnum = 100_000_001
num = 1_000_000_001


def even_num_squares():
    for i in range(0, num, 2):
        yield i


a = iter(even_num_squares())

print(
    list(
        map(
            lambda _: next(a) ** 2,
            a
        )
    )
)
# 1
# def square(limit):
#     # return [i ** 2 for i in range(limit) if i % 2 == 0]
#     # return [i * i for i in range(2, limit, 2)]
#     return [n for n in even_num_squares(limit)]


# print(square(midnum))
# 2
# def square(nums):
#     a = [i for i in range(nums) if i % 2 == 0]
#     return [i ** 2 for i in range(nums)]
#
# print(square(smallnum))

# 3
# square = [i for i in range(smallnum) if i % 2 == 0]
# for i in square:
#     print(i * i)

# 4
# def even_num_squares():
#     for i in range(0, midnum, 2):
#         yield i * i
#
# a = iter(even_num_squares())
#
# while True:
#     print(next(a))

print((time.time() - start) * 10 ** 3, "ms")
