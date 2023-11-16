# Павлов Д.В. ИУ7-13Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G.

# Блок ввода матриц
n = int(input("Введите кол-во строк матриц: "))
md = int(input("Введите кол-во столбцов матрицы d: "))
mz = int(input("Введите кол-во столбцов матрицы z: "))

# Блок проверки на правильность ввода
while n <= 0 or md <= 0 or mz <= 0:
    print('Ошибка размер должен быть больше 0')
    n = int(input("Введите кол-во строк матриц: "))
    md = int(input("Введите кол-во столбцов матрицы d: "))
    mz = int(input("Введите кол-во столбцов матрицы z: "))

# Блок ввода матрицы d
d = []
print("Введите матрицу d:")
for i in range(n):
    row = []
    for j in range(md):
        elem = int(input(f"Введите элемент матрицы d с индексом: {i} {j}: "))
        row.append(elem)
    d.append(row)

# Блок ввода матрицы z
z = []
print("Введите матрицу z:")
for i in range(n):
    row = []
    for j in range(mz):
        elem = int(input(f"Введите элемент матрицы z с индексом: {i} {j}: "))
        row.append(elem)
    z.append(row)

print("Матрица z")
for i in range(n):
    tmp = ''
    for j in range(mz):
        tmp += f'{z[i][j]:^6}'
    print(tmp)

print("Матрица d до преобразования")
for i in range(n):
    tmp = ''
    for j in range(md):
        tmp += f'{d[i][j]:^6}'
    print(tmp)

g = []

# Блок создания массива g
for i in range(n):
    c = 0
    s_z = sum(z[i])
    for j in range(md):
        if d[i][j] > s_z:
            c += 1
    g.append(c)

m_g = max(g)

# Блок преобразования матрицы d
for i in range(n):
    for j in range(md):
        d[i][j] = m_g * d[i][j]

print("Матрица d после преобразования")
for i in range(n):
    tmp = ''
    for j in range(md):
        tmp += f'{d[i][j]:^6}'
    print(tmp)

print(f"Массив g: {' '.join(map(str, g))}")
