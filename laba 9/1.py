# Павлов Д. В. ИУ7-13Б
#  Даны массивы D и F. Сформировать матрицу A по формуле a[j][k] = sin(dj+fk).
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.
# В AV записывать особое значение при отсутствии положительных элементов

from math import sin

# Блок ввода массивов d and f
d = list(map(float, input("Введите массив d: ").split()))
f = list(map(float, input("Введите массив f: ").split()))

a = []  # создание массива a
av = []  # создание массива av
l = []  # создание массива l

# Блок вычисления и добавления элементов матриц
for j in range(len(d)):
    row = []
    for k in range(len(f)):
        row.append(sin(d[j] + f[k]))
    c_positve = 0
    s = 0
    c = 0
    for i in row:
        if i > 0:
            c_positve += 1
            s += i
    if c_positve > 0:
        av_row = s / c_positve
    else:
        av_row = None
    for i in row:
        if av_row is not None and i < av_row:
            c += 1
    av.append(av_row)
    l.append(c)
    a.append(row)

# Блок вывода матриц
tmp = f'{"i/j":^4}|'
for j in range(len(f)):
    tmp += f'{j + 1:^16}'
tmp += f'|{"AV":^17}|'
tmp += f'{"L":^16}|'
width = len(tmp)
print('-' * width)
print(tmp)
print('-' * width)
for i in range(len(d)):
    tmp = f'{i + 1:^4}|'
    for j in range(len(f)):
        tmp += f'{a[i][j]:^16.5g}'
    if av[i] is not None:
        tmp += f'|{av[i]:^17.5g}|'
    else:
        tmp += f'|{"Неопределенно":^17}|'
    tmp += f'{l[i]:^16.5g}|'
    print(tmp)
print('-' * width)

