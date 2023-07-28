
'''
1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
представление. Функцию hex используйте для проверки своего результата.
2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
'''


NUMBER = 16
lst = []


def dz_1():

    num = int(input(("Введите целое число... ")))
    while True:
        res_ost = num % NUMBER
        if res_ost == 0:
            break

        match res_ost:
            case 10:
                res_ost = "A"
            case 11:
                res_ost = "B"
            case 12:
                res_ost = "C"
            case 13:
                res_ost = "D"
            case 14:
                res_ost = "E"
            case 15:
                res_ost = "F"

        lst.append(str(res_ost))
        num = num // NUMBER

    str_lst = "".join(lst[::-1])
    print(str_lst)




"дроби"

import fractions


f1 = fractions.Fraction(2, 3)
f2 = fractions.Fraction(3, 7)
print('{} + {} = {}'.format(f1, f2, f1 + f2))
print('{} - {} = {}'.format(f1, f2, f1 - f2))
print('{} * {} = {}'.format(f1, f2, f1 * f2))
print('{} / {} = {}'.format(f1, f2, f1 / f2))



