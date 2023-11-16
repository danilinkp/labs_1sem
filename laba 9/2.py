# Павлов Д.В. ИУ7-13Б
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки.

# Блок ввода матрицы
n = int(input("Введите размер квадратной матрицы: "))

# Блок проверки на правильность ввода
while n <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите размер матрицы: '))

print("Введите матрицу:")
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        elem = int(input(f"Введите элемент матрицы с индексом: {i} {j}: "))
        row.append(elem)
    matrix.append(row)


print("Исходная матрица:")
for i in range(n):
    tmp = ''
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}'
    print(tmp)

# matrix = list(zip(*matrix[::-1]))
for i in range(n // 2):
    for j in range(i, n - i - 1):
        matrix[i][j], matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] = matrix[n - 1 - j][i], \
            matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i], matrix[i][j]

print("Промежуточная матрица:")
for i in range(n):
    tmp = ''
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}'
    print(tmp)

# matrix = list(zip(*[i[::-1] for i in matrix]))
for i in range(n // 2):
    for j in range(i, n - i - 1):
        matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = matrix[j][n - 1 - i], \
            matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i], matrix[i][j]

print("Итоговая матрица:")
for i in range(n):
    tmp = ''
    for j in range(n):
        tmp += f'{matrix[i][j]:^6}'
    print(tmp)
