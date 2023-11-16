# Павлов Д.В. ИУ7-13Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.


# Блок ввода размеров матриц А и В
n, m = map(int, input("Введите размер матрицы: ").split())

# Блок проверки на правильность ввода
while n <= 0 or m <= 0:
    print('Ошибка размер должен быть больше 0')
    n, m = map(int, input("Введите размер матрицы: ").split())

# Блок ввода матриц А и В
print("Введите матрицу A:")
matrix_a = [[int(elem) for elem in input().split()] for row in range(n)]

print("Введите матрицу B:")
matrix_b = [[int(elem) for elem in input().split()] for row in range(n)]

# создание матрицы C
matrix_c = []
for i in range(n):
    c_i = []
    for j in range(m):
        c_i.append(matrix_a[i][j] * matrix_b[i][j])
    matrix_c.append(c_i)

# создание матрицы v
v = []
for i in range(m):
    s = 0
    for j in range(n):
        s += matrix_c[j][i]
    v.append(s)

# Блок вывода матриц и массивов
print("Матрица A")
for i in range(n):
    tmp = ''
    for j in range(n):
        tmp += f'{matrix_a[i][j]:^6}'
    print(tmp)

print("Матрица B")
for i in range(n):
    tmp = ''
    for j in range(n):
        tmp += f'{matrix_b[i][j]:^6}'
    print(tmp)

print("Матрица C")
for i in range(n):
    tmp = ''
    for j in range(n):
        tmp += f'{matrix_c[i][j]:^6}'
    print(tmp)

print(f"Массив v: {' '.join(map(str, v))}")
