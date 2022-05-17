# #todo: Найти сумму элементов матрицы,
# Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21
#
# >>> msum(load_matrix('matrix.txt'))
# 423


matrix = [[1, 2, 3], [4, 5, 6]]  #ее смог. не понимаю логику

def msum(matrix):
    columns = len(matrix)
    strings = len(matrix[1])
    T = [[matrix[j][i] for j in range(columns)] for i in range(strings)]
    return sum(list(T))
print(f"Сумма матрицы {msum(matrix)}")