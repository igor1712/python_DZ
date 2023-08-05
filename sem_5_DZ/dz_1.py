
"""Напишите функцию которая принимает на вход строку и возращает кортеж из трех элементов
путь, имя файла, расширение файла """

def my_func(link: str) -> tuple:
    link = link.decode("utf-8")
    suffix, *data, name = link.split("\\")
    pash = suffix + ' '.join(data)
    *_, rash = name.split('.')
    return pash, name, rash



text = b"C:\Users\Admin\PycharmProjects\pythonProjectj\geeekbrains\sem_5_DZ\dz_1.py"
print(my_func(text))
