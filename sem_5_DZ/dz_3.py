"""Создайте функцию генератор чисел Фибоначчи"""


def fib(num: int):
    a, b = 0, 1
    for i in range(num):
        yield a
        a, b = b, a+b

print(*fib(13))
