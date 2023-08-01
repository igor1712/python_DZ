

"""Напишите функцию для транспонирования матрицы.
Пример: [[1, 2, 3],
        [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
"""


def transp_matrix(args):
    return list(map(list, zip(*args)))

matrix = [[1, 2, 3], [4, 5, 6]]
print(transp_matrix(matrix))

