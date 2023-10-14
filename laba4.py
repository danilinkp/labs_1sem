#  Павлов Д В ИУ7-13Б

# Программа, которая для заданных функций y1 = x^2 - sin(pi * x) и
# y2 = 7.5x^4 - 11x^3 + 3.8x^2 + 0.4x - 0.98) выводит таблицу значений этих
# функций на некотором отрезке. Запрашивает кол-во засечек (от 4 до 8)
# и строит график одной из них (y1)
# 1) определить значения 𝑦 и x, при котором оно достигается

from math import sin, pi

# Блок ввода значений
start_x = float(input('Введите начальное значение аргумента: '))
end_x = float(input('Введите конечное значение аргумента: '))
h = float(input('Введите шаг разбиения данного отрезка: '))

# Блок повторного ввода при неправильных значений

if start_x >= end_x:
    print('Начальное значение не может быть больше или равно конечному')
    start_x = float(input('Введите начальное значение аргумента: '))
    end_x = float(input('Введите конечное значение аргумента: '))
elif h <= 0:
    print('Шаг не может быть меньше или равнен нулю')
    h = float(input('Введите шаг разбиения данного отрезка: '))
elif end_x - start_x < h:
    print('Шаг не может быть больше разницы конечного и начального значения аргумента')
    h = float(input('Введите шаг разбиения данного отрезка: '))

eps = 1e-12
x = start_x
y1_min = float('+inf')
y2_min = float('+inf')
y1_max = float('-inf')
x_min = 0

# Блок вывода таблицы
print("-" * 46)
print(f'| {"x":^12} | {"y1":^12} | {"y2":^12} |')
print("-" * 46)

while x <= (end_x + eps):
    y1 = x ** 2 - sin(pi * x)
    y2 = 7.5 * x ** 4 - 11 * x ** 3 + 3.8 * x ** 2 + 0.4 * x - 0.98
    if abs(x) < eps:
        print(f"| {0.0:^12.5g} | {y1:^12.5g} | {y2:^12.5g} |")
    else:
        print(f"| {x:^12.5g} | {y1:^12.5g} | {y2:^12.5g} |")
    if y1 < y1_min:
        y1_min = y1
        x_min = x
    if y2 < y2_min:
        y2_min = y2
    if y1 > y1_max:
        y1_max = y1
    x += h
print("-" * 46)

# Блок ввода количества засечек
scale = int(input('Введите количество засечек: '))  # кол-во засечек

if not (4 <= scale <= 8):
    print('Количество засечек должно быть от 4 до 8')
    scale = int(input('Введите количество засечек: '))

delta = (y1_max - y1_min) / (scale - 1)  # число между засечками
width = 100  # ширина поля
point_scale = width / (y1_max - y1_min)  # коэффицент маcштаба на поле
chart_header = ' ' * 13  # заголовок графика
y = y1_min
i = 0

# формирование заголовка графика
while i < scale:
    if i == 0:
        chart_header += f"{y: <{int(width / scale)}.5g}"
    elif i == scale - 1:
        chart_header += f'{y: >{int(width / scale)}.5g}'
    else:
        if width / scale == 0:
            chart_header += f"{y: ^{int(width / scale)}.5g}"
        else:
            chart_header += f"{y: ^{int(width / scale) + 1}.5g}"
    y += delta
    i += 1
print(chart_header)

# количества пробелов до OX
ox = 13 + (int(point_scale * (0 - y1_min)) - 1)
x = start_x

while x <= (end_x + eps):
    y1 = x ** 2 - sin(pi * x)

    # количества пробелов до звездочки
    spaces_before = (int(point_scale * (y1 - y1_min)) - 1)

    # количества пробелов после звездочки
    spaces_after = (width - 12 - int(point_scale * (y1 - y1_min)) - 1)

    # график пересекает ОX
    if y1_min <= 0 <= y1_max:
        if abs(x) <= eps:
            s = f'{0.0:<12.5g}|' + ' ' * spaces_before + '*' + ' ' * spaces_after
        else:
            s = f'{x:<12.5g}|' + ' ' * spaces_before + '*' + ' ' * spaces_after
        if s[ox] != '*':
            s = s[:ox] + '|' + s[ox + 1:]

        print(s)

    # график не пересекает ОX
    else:
        if abs(x) < eps:
            print(f'{0.0:<12.5g}|' + ' ' * spaces_before + '*' + ' ' * spaces_after)
        else:
            print(f'{x:<12.5g}|' + ' ' * spaces_before + '*' + ' ' * spaces_after)

    x += h

print('\n')
print(f'Минимальное значение y1 = {y1_min:.5g} при x_min = {x_min:.5g}')
print(f'Минимальное значение y2 = {y2_min:.5g}')
