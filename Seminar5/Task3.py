"""Создайте функцию генератор чисел Фибоначчи"""

def fib1(num):
    result1 = 1
    result2 = 1
    if num == 0 or num == 1:
        return 1
    else:
        for i in range(num-2):
            if i % 2 == 0:
                result1 += result2
                if i == (num - 3):
                    yield result1
            else:
                result2 += result1
                if i == (num - 3):
                    yield result2


a = iter(fib1(10))
print(next(a))




# def fib(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1
#     else:
#         return fib(num - 2) + fib(num - 1)