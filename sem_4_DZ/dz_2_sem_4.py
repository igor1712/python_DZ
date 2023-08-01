

"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте
его строковое представление.
 Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}"""


def func(*, res: int, reverse: list[int]) -> tuple[int:str] | tuple[str:str]:
    new_tuple = {}
    new_tuple[res] = "res"
    new_tuple[str(reverse)] = "reverse"
    return new_tuple


print(func(res=1, reverse=[1, 2, 3]))
