# Павлов Д.В. ИУ7-13Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования

# Блок ввода матрицы
n, m = map(int, input("Введите размер матрицы: ").split())

# Блок проверки на правильность ввода
while n <= 0 or m <= 0:
    print('Ошибка размер должен быть больше 0')
    n, m = map(int, input("Введите размер матрицы: ").split())

# Блок ввода матрицы
matrix = []
print("Введите матрицу:")
for i in range(n):
    row = []
    for j in range(m):
        elem = input(f"Введите элемент матрицы с индексом: {i} {j}: ")
        row.append(elem)
    matrix.append(row)

vowels = 'eyuioa'  # гласные английского алфавита

print("Матрица до преобразования")
for i in range(n):
    tmp = ''
    for j in range(m):
        tmp += f'{matrix[i][j]:^6}'
    print(tmp)
print()
# Блок изменения матрицы
for i in range(n):
    for j in range(m):
        if matrix[i][j].lower() in vowels:
            matrix[i][j] = '.'

# вывод матрицы после преобразования
print("Матрица после преобразования")
for i in range(n):
    tmp = ''
    for j in range(m):
        tmp += f'{matrix[i][j]:^6}'
    print(tmp)

