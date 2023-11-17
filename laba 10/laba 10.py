# Павлов Даниил ИУ7-13Б
# Написать программу для вычисления приближённого значения интеграла
# известной функции двумя разными методами:
# 1) Метод левых прямоугольников
# 2) Метод 3/8
# Далее на основе известной, заданной в программе, первообразной определить, какой
# метод является наиболее точным. Для этого требуется вычислить и отобразить
# абсолютную и относительную погрешности каждого из четырёх измерений. Метод,
# измерение которого с одним из разбиений дало самое близкое к первообразной
# значение, считается наиболее точным.
# Затем для другого, менее точного метода, итерационно вычислить количество участков
# разбиения, для которого интеграл будет вычислен с заданной точностью

from math import *


def f(x: float):
    """Функция вычисления заданной математической функции"""
    try:
        return x ** 2
    except Exception:
        return "Функция в этой точке неопределена"


def F(x: float):
    """Функция вычисления заданной первообразной"""
    try:
        return (x ** 3) / 3
    except Exception:
        return "Первообразная в этой точке неопределена"


def method_left_rectangles(start: float, end: float, n: int, f):
    """Функция подсчёта интеграла с помощью метода левых треугольников"""
    if n == 0:
        return "Количество участков разбиения должно быть больше нуля"
    h = (end - start) / n  # Шаг разбиения
    x = start  # Точка вычисления
    integral = 0  # значение интеграла
    for i in range(1, n):
        integral += h * f(x)
        x += h
    return integral


def method_three_eights(start: float, end: float, n: int, f):
    """Функция подсчёта интеграла с помощью метода 3/8"""
    if n == 0:
        return "Количество участков разбиения должно быть больше нуля"
    h = (end - start) / n  # Шаг разбиения
    x0 = start  # Точка вычисления
    x1 = start + h
    integral = 0  # значение интеграл
    for i in range(n):
        integral += h * (f(x0) + 3 * f((2 * x0 + x1) / 3) + 3 * f((x0 + 2 * x1) / 3) + f(x1)) / 8
        x0 += h
        x1 += h
    return integral


def make_table(name: str, first_value: float, second_value: float, third_value: float, fourth_value: float):
    """Функция для создания таблицы вычисленных значений"""
    print(name)
    print('-' * 67)
    head = '|' + " " * 27 + '|' + f"{'N1':^18}" + '|' + f"{'N2':^18}" + '|'
    print(head)
    print('-' * 67)
    print('|' + f"{'Метод левых треугольников':^27}" + '|' + f"{first_value:^18.5g}" + '|' + \
          f"{second_value:^18.5g}" + '|')
    print('-' * 67)
    print('|' + f"{'Метод 3/8':^27}" + '|' + f"{third_value:^18.5g}" + \
          '|' + f"{fourth_value:^18.5g}" + '|')
    print('-' * 67 + '\n')


start = end = n1 = n2 = None  # Начало и конец отрезка интегрирования кол-ва участков разбиения соответственно
while start is None or end is None:
    try:
        start, end = map(float, input("Введите начало и конец отрезка интегрирования: ").split())
        if start >= end:
            start = end = None
            raise Exception
    except Exception:
        print('Началом и концом отрезка интегрирования могут быть только вещественные числа' +
              ' и начало должно быть строго меньше чем конец' +
              '\nПовторите попытку ввода:')

while n1 is None or n2 is None:
    try:
        n1, n2 = map(int, input("Введите n1 и n2 (количества участков разбиения): ").split())
        if n1 <= 0 or n2 <= 0:
            n1 = n2 = None
            raise Exception
    except Exception:
        print('Количества участков разбиения (n1 и n2) могут быть только целые числа больше 0!' +
              '\nПовторите попытку ввода:')
# значения интегралов вычисленного методом левых треугольников
first_integral_N1 = method_left_rectangles(start, end, n1, f)
first_integral_N2 = method_left_rectangles(start, end, n2, f)

# значения интегралов вычисленного методом 3/8
second_integral_N1 = method_three_eights(start, end, n1, f)
second_integral_N2 = method_three_eights(start, end, n2, f)

print()
make_table(name="Значение вычисленных интегралов заданными методами:", first_value=first_integral_N1,
           second_value=first_integral_N2,
           third_value=second_integral_N1, fourth_value=second_integral_N2)

# Вычсиление интеграла с помощью первообразной
exact_integral = F(end) - F(start)
print(f"Значение интеграла вычисленного с помощью первообразной: {exact_integral:.5g}\n")

# Вычисления абсолютной погрешности и их вывод
first_absolute_error_N1 = abs(exact_integral - first_integral_N1)
first_absolute_error_N2 = abs(exact_integral - first_integral_N2)
second_absolute_error_N1 = abs(exact_integral - second_integral_N1)
second_absolute_error_N2 = abs(exact_integral - second_integral_N2)

make_table(name="Абсолютная погрешность вычисления", first_value=first_absolute_error_N1,
           second_value=first_absolute_error_N2,
           third_value=second_absolute_error_N1, fourth_value=second_absolute_error_N2)

# Вычисления относительной погрешности и их вывод
if exact_integral != 0:
    first_relative_error_N1 = first_absolute_error_N1 / exact_integral
    first_relative_error_N2 = first_absolute_error_N2 / exact_integral
    second_relative_error_N1 = second_absolute_error_N1 / exact_integral
    second_relative_error_N2 = second_absolute_error_N1 / exact_integral

    make_table(name="Относительная погрешность вычисления", first_value=first_relative_error_N1,
               second_value=first_relative_error_N2,
               third_value=second_relative_error_N1, fourth_value=second_relative_error_N2)
else:
    print('Ошибка! При вычисление относительной погрешности произошла ошибка (деление на ноль)\n')

error_rates = [first_absolute_error_N1, first_absolute_error_N2, second_absolute_error_N1, second_absolute_error_N2]

# Нахождение наименее точного метода
if max(error_rates) == first_absolute_error_N1 or max(error_rates) == first_absolute_error_N2:
    inexact_method = method_left_rectangles
    inexact_method_name = 'Метод Левых прямоугольников'
else:
    inexact_method = method_three_eights
    inexact_method_name = 'Метод 3/8'

print(f"Наименее точный метод это: {inexact_method_name}")

eps = float(input("Введите точность измерения для наименее точного метода: "))

n = 2  # кол-во участков разбиения
integral_1 = inexact_method(start, end, n, f)
integral_2 = inexact_method(start, end, 2 * n, f)

# Подсчет участков разбиения
while (abs(integral_1 - integral_2)) >= eps:
    n += 1
    integral_1 = integral_2
    integral_2 = inexact_method(start, end, 2 * n, f)

print(f"Количество участков разбиения: {n}")
print(f"Приблеженное значение интеграла: {inexact_method(start, end, n, f):.5g}")
