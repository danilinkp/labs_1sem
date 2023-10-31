# Павлов Д.В. ИУ7-13Б
# Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.

# Блок ввода матрицы
n, m = map(int, input("Введите размер матрицы (сначала кол-во строк, затем столбоцов): ").split())

while n <= 0 or m <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))

print("Введите матрицу:")
matrix = [[int(elem) for elem in input().split()] for row in range(n)]

max_negative = -1
min_negative = -1
c_min_negative = m + 1
c_max_negative = 0

# Блок вычисления
for i in range(n):
    count_negatives = 0
    for elem in matrix[i]:
        if elem < 0:
            count_negatives += 1
    if count_negatives > c_max_negative:
        max_negative = i
        c_max_negative = count_negatives
    if count_negatives < c_min_negative:
        min_negative = i
        c_min_negative = count_negatives

# Блок перестановки
matrix[max_negative], matrix[min_negative] = matrix[min_negative], matrix[max_negative]

# Блок вывода
if max_negative == -1 or min_negative == -1:
    print('Отрицательных элементов нет')
else:
    print("Полученная матрица:")

    for i in range(n):
        tmp = ''
        for j in range(m):
            tmp += f'{matrix[i][j]:^6}'
        print(tmp)