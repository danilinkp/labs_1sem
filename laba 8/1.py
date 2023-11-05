# Павлов Д.В. ИУ7-13Б
# Найти строку, имеющую наибольшее количество чётных элементов

# Блок ввода матрицы
n, m = map(int, input("Введите размер матрицы: ").split())

# Блок проверки на правильность ввода
while n <= 0 or m <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))

print("Введите матрицу:")
matrix = [[int(elem) for elem in input().split()] for row in range(n)]

max_even = 0  # кол-во наибольших четных
max_row = -1  # индекс наибольшей строки

# Блок вычисления
for i in range(n):
    c = 0
    for elem in matrix[i]:
        if elem % 2 == 0:
            c += 1
    if c > max_even:
        max_row = i
        max_even = c

# Блок вывода
if max_row == -1:
    print('Нужая строка не найдена')
else:
    print(f"Строка {max_row} имеющая наибольшее кол-во четных чисел: {' '.join(map(str, matrix[max_row]))}")
