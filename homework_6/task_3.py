def is_prime(argument: int) -> bool:
    if argument not in range(2, 1000):
        return False
    if argument % 2 == 0 and argument > 2:
        return False
    for i in range(3, argument // 2, 2):
        if (argument % i) == 0:
            return False
    return True

# import math


# def is_prime(n):
#     if n < 2:
#         return False
#     nums = [i for i in range(n + 1)]
#     for i in range(2, math.ceil(math.sqrt(n) + 1)):
#         for j in range(i, n + 1):
#             if nums[j] % i == 0 and nums[j] != i:
#                 nums[j] //= i
#     primes = [x for x in range(n + 1) if nums[x] == x]
#     print(primes)
#     return n in primes


assert is_prime(1000) is False
assert is_prime(2) is True
assert is_prime(1) is False
assert is_prime(0) is False
assert is_prime(-5) is False
assert is_prime(98343) is False
assert is_prime(507) is False
assert is_prime(37) is True
