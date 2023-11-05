# Павлов Д.В. ИУ7-13Б
# Выполнить транспонирование квадратной матрицы

# Блок ввода матрицы
n = int(input("Введите размер квадратной матрицы: "))

# Блок проверки на правильность ввода
while n <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите размер матрицы: '))

print("Введите матрицу:")
matrix = [[int(elem) for elem in input().split()] for row in range(n)]

# Блок вычисления
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Блок вывода
print("Полученная матрица:")
for i in range(n):
    tmp = ''
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}'
    print(tmp)

