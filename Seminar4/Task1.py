"""Напишите функцию для транспонирования матрицы . """


def matrix_trans(matrix):
    new_matrix = []
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(matrix[j][i])
        new_matrix.append(temp)
    return new_matrix
m = [[1,2,3],[4,5,6],[7,8,9]]
print(f'{m[0]}\n{m[1]}\n{m[2]}\n')
print(matrix_trans(m))
