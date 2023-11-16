n = int(input("Введите размер квадратной матрицы: "))

while n <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input('Введите размер матрицы: '))

print("Введите матрицу")
matrix = [[int(i) for i in input().split()] for i in range(n)]

for i in range(n):
    # for j in range(n):
    for j in range(n - i, n):
        # if i > n - j - 1:
        matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], 0

for i in matrix:
    print(i)
