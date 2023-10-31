# Павлов Д.В. ИУ7-13Б
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю.

# Блок ввода матрицы
n = int(input("Введите размер квадратной матрицы: "))

while n <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите размер матрицы: '))

print("Введите матрицу:")
matrix = [[int(elem) for elem in input().split()] for row in range(n)]

s_max = float("-inf")
s_min = float("+inf")

# Блок вычисления
for i in range(n):
    for j in range(n):
        if j > i:
            if matrix[i][j] > s_max:
                s_max = matrix[i][j]
        if (n - j - 1) < i:
            if matrix[i][j] < s_min:
                s_min = matrix[i][j]

# Блок вывода
print(f"Максимальное над главной: {s_max}")
print(f"Минимальное под побочной: {s_min}")
