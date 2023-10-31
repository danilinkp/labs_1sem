# Павлов Д.В. ИУ7-13Б
# Найти столбец, имеющий наибольшее количество нулевых элементов.

# Блок ввода матрицы
n, m = map(int, input("Введите размер матрицы (сначала кол-во строк, затем столбоцов): ").split())

while n <= 0 or m <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))

print("Введите матрицу:")
matrix = [[int(elem) for elem in input().split()] for row in range(n)]

max_col = []
c_max_nulls = -1

# Блок вычисления
for i in range(m):
    cur_col = []
    for j in range(n):
        cur_col.append(matrix[j][i])
    count_nulls = len([i for i in cur_col if i == 0])
    if count_nulls > c_max_nulls:
        c_max_nulls = count_nulls
        max_col = cur_col

# Блок вывода
if max_col:
    print(f"Столбец имеющий наибольшее кол-во нулевых элементов: {' '.join(map(str, max_col))}")
else:
    print("Нужный столбец не найден")
