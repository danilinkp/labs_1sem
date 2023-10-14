#  Павлов Д В ИУ7-13Б
# Написать программу, которая по введенным целочисленным
# координатам трех точек на плоскости вычисляет длины сторон
# образованного треугольника и длину медианы, проведенной из
# наименьшего угла.
# Определить, является ли треугольник прямоугольным.
# Далее вводятся координаты точки. Определить, находится ли
# точка внутри треугольника. Если да, то найти расстояние от точки до ближайшей стороны треугольника.

# Блок ввода значений трех точек треугольника
x1, y1 = map(int, input("Введите координаты точек х1, y1 через пробел: ").split())
x2, y2 = map(int, input("Введите координаты точек х2, y2 через пробел: ").split())
x3, y3 = map(int, input("Введите координаты точек х3, y3 через пробел: ").split())

# Блок вычисления сторон треугольника и медианы, опущенной на эту сторону
a1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
med1 = ((x3 - ((x1 + x2) / 2)) ** 2 + (y3 - ((y1 + y2) / 2)) ** 2) ** 0.5

a2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
med2 = ((x1 - ((x3 + x2) / 2)) ** 2 + (y1 - ((y3 + y2) / 2)) ** 2) ** 0.5

a3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
med3 = ((x2 - ((x1 + x3) / 2)) ** 2 + (y2 - ((y1 + y3) / 2)) ** 2) ** 0.5

# Блок определения треугольник ли это
if (y3 - y1) * (x2 - x1) == (x3 - x1) * (y2 - y1):
    print("Это не треугольник")

else:
    # Блок нахождения минимальной стороны треугольника и медианы из меньшего угла
    min_side = 0
    min_med = 0
    if a1 <= a2 <= a3 or a1 <= a3 <= a2:
        min_side = a1
        min_med = med1
    if a2 <= a1 <= a3 or a2 <= a3 <= a1:
        min_side = a2
        min_med = med2
    if a3 <= a2 <= a1 or a3 <= a1 <= a2:
        min_side = a3
        min_med = med3

    # Блок вывода сторон треугольника м медианы
    print(f"Длина стороны 1 треугольника = {a1:.8g}")
    print(f"Длина стороны 2 треугольника = {a2:.8g}")
    print(f"Длина стороны 3 треугольника = {a3:.8g}")
    print(f"Длина медианы, проведенной из наименьшего угла = {min_med:.8g}")

    # Блок определения прямоугольный треугольник или нет
    eps = 1e-8
    if abs((a1 ** 2 + a2 ** 2) - (a3 ** 2)) <= eps or abs((a3 ** 2 + a2 ** 2) - (a1 ** 2)) <= eps or abs(
            (a1 ** 2 + a3 ** 2) - (a2 ** 2)) <= eps:
        print('Треугольник является прямоугольным')
    else:
        print('Треугольник не прямоугольный')

    # Блок ввода координат точки в пространстве
    x, y = map(float, input("Введите координаты точки через пробел: ").split())

    # Блок вычисления длин от каждой точки треугольника к заданной точке
    b = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
    c = ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5
    d = ((x3 - x) ** 2 + (y3 - y) ** 2) ** 0.5

    # Блок подсчета площадей треугольников по формуле герона и расстояния от этой точки к стороне
    p = (a1 + a2 + a3) / 2
    s = (p * (p - a1) * (p - a2) * (p - a3)) ** 0.5

    p1 = (a1 + b + c) / 2
    s1 = (p1 * (p1 - a1) * (p1 - b) * (p1 - c)) ** 0.5
    h1 = s1 * 2 / a1

    p2 = (a2 + d + c) / 2
    s2 = (p2 * (p2 - a2) * (p2 - d) * (p2 - c)) ** 0.5
    h2 = s2 * 2 / a2

    p3 = (a3 + b + d) / 2
    s3 = (p3 * (p3 - a3) * (p3 - b) * (p3 - d)) ** 0.5
    h3 = s3 * 2 / a3

    # Блок определения минимальной высоты
    min_h = 0
    if h1 <= h2 <= h3 or h1 <= h3 <= h2:
        min_h = h1
    if h2 <= h1 <= h3 or h2 <= h3 <= h1:
        min_h = h2
    if h3 <= h2 <= h1 or h3 <= h1 <= h2:
        min_h = h3

    # Блок вывода внутри ли точка или нет
    if abs(s1 + s2 + s3 - s) <= eps:
        print("Точка внутри треугольника")
        print(f"Расстояние от точки до ближайшей стороны треугольника: {min_h:.7g}")
    else:
        print("Точка вне треугольника")
