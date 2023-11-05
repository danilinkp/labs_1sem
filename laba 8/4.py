# Павлов Д.В. ИУ7-13Б
# Переставить местами столбцы с максимальной и минимальной суммой элементов

# Блок ввода матрицы
n, m = map(int, input("Введите размер матрицы (сначала кол-во строк, затем столбоцов): ").split())

# Блок проверки на правильность ввода
while n <= 0 or m <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))

print("Введите матрицу:")
matrix = [[int(elem) for elem in input().split()] for row in range(n)]

max_col = 0
min_col = 0
s_max = float("-inf")
s_min = float("+inf")

# Блок вычисления
for i in range(m):
    cur_col = []
    for j in range(n):
        cur_col.append(matrix[j][i])
    s = sum(cur_col)
    if s > s_max:
        s_max = s
        max_col = i
    if s < s_min:
        s_min = s
        min_col = i

for i in range(n):
    matrix[i][max_col], matrix[i][min_col] = matrix[i][min_col], matrix[i][max_col]

# Блок вывода
if max_col == min_col:
    print("Матрица не изменилась")
    for i in range(n):
        tmp = ''
        for j in range(m):
            tmp += f'{matrix[i][j]:^6}'
        print(tmp)
else:
    print("Полученная матрица:")
    for i in range(n):
        tmp = ''
        for j in range(m):
            tmp += f'{matrix[i][j]:^6}'
        print(tmp)
