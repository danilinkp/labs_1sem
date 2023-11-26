# Павлов Д. В. ИУ7-13б

# Метод "Расчёсок"
# Написать программу для демонстрации работы метода сортировки (по варианту) на
# примере массива целых чисел.
# Программа должна состоять из двух частей (этапов работы) и выполнять два действия
# последовательно:
# 1. сначала отсортировать заданный пользователем массив для доказательства корректности работы алгоритма;
# 2. затем составить таблицу замеров времени сортировки списков трёх различных
# (заданных пользователем) размерностей и количества перестановок в каждом из них.

import time
from random import randint


def input_array() -> list:
    """Функция ввода массива"""
    array = None
    while array is None:
        try:
            array = list(map(int, input("Введите массив целых чисел: ").split()))
            if len(array) == 0:
                array = None
                raise ValueError
        except ValueError:
            print("Числа в массиве должны быть целыми")
    return array


def comb_sort(arr: list) -> int:
    """Функция сортировки расчёской"""
    swaps = 0
    n = len(arr)
    step = len(arr)
    factor = 1.247331
    is_swapped = False
    while step > 1 or is_swapped:
        if step > 1:
            step = int(step / factor)
        is_swapped = False
        i = 0
        while (i + step) < n:
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                is_swapped = True
                swaps += 1
            i += step
    return swaps


def input_sizes() -> tuple:
    """Функция ввода размеров массивов"""
    n1 = n2 = n3 = None
    while n1 is None or n2 is None or n3 is None:
        try:
            n1, n2, n3 = map(int, input("Введите размеры трех массивов через пробел: ").split())
            if n1 < 1 or n2 < 1 or n3 < 1:
                n1 = n2 = n3 = None
                raise ValueError
        except ValueError:
            print("Размеры должны быть целыми положительными числами и кол-во вводимых значений должно быть равно 3")
    return n1, n2, n3


def sorted_arr(n: int) -> tuple:
    """Функция вычисления времени и кол-ва перестановок для отсортированного массива"""
    arr = [i for i in range(10, n + 11)]
    start_time = time.time()
    permutations = comb_sort(arr)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutations


def reverse_sorted_arr(n: int) -> tuple:
    """Функция вычисления времени и кол-ва перестановок для отсортированного в обратном порядке массива"""
    arr = [i for i in range(n, 0, -1)]
    start_time = time.time()
    permutations = comb_sort(arr)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, permutations


def random_arr(n: int) -> tuple:
    """Функция вычисления времени и кол-ва перестановок для случайного массива"""
    arr = [randint(-100000, 100000) for i in range(n)]
    start_time = time.time_ns()
    permutations = comb_sort(arr)
    end_time = time.time_ns()
    total_time = end_time - start_time
    return total_time, permutations


def make_table(*args):
    """Функция создания таблицы"""
    researches = [i for i in args]
    print('-' * 103)
    print('|' + ' ' * 20 + '|' + f'{"N1":^26}' + '|' + f'{"N2":^26}' + '|' + f'{"N3":^26}' + '|')
    print('-' * 103)
    print(
        '|' + ' ' * 20 + '|' + f'{"время (сек)":^11}' + '|' + f'{"перестановки":^14}' + '|' + f'{"время (сек)":^11}' + '|' +
        f"{'перестановки':^14}" + '|' + f'{"время (сек)":^11}' + '|' + f"{'перестановки':^14}" + '|')
    print('-' * 103)
    print(
        '|' + f'{"Упорядоченный":^20}' + '|' + f'{researches[0][0]:^11}' + '|' + f'{researches[0][1]:^14.5g}' + '|'
        + f'{researches[1][0]:^11.5g}' + '|' + f"{researches[1][1]:^14.5g}" +
        '|' + f'{researches[2][0]:^11.5g}' + '|' + f"{researches[2][1]:^14.5g}" + '|')
    print('-' * 103)
    print(
        '|' + f'{"Oбратный":^20}' + '|' + f'{researches[3][0]:^11.5g}' + '|' + f'{researches[3][1]:^14.5g}' + '|'
        + f'{researches[4][0]:^11.5g}' + '|' + f"{researches[4][1]:^14.5g}" +
        '|' + f'{researches[5][0]:^11.5g}' + '|' + f"{researches[5][1]:^14.5g}" + '|')
    print('-' * 103)
    print(
        '|' + f'{"Случайный":^20}' + '|' + f'{researches[6][0]:^11.5g}' + '|' + f'{researches[6][1]:^14.5g}' + '|'
        + f'{researches[7][0]:^11.5g}' + '|' + f"{researches[7][1]:^14.5g}" +
        '|' + f'{researches[8][0]:^11.5g}' + '|' + f"{researches[8][1]:^14.5g}" + '|')
    print('-' * 103)


def main():
    arr = input_array()
    comb_sort(arr)
    print(f"Отсортированный массив: {' '.join(map(str, arr))}")

    n1, n2, n3 = input_sizes()

    t1, k1 = sorted_arr(n1)
    t4, k4 = reverse_sorted_arr(n1)
    t7, k7 = random_arr(n1)

    t2, k2 = sorted_arr(n2)
    t5, k5 = reverse_sorted_arr(n2)
    t8, k8 = random_arr(n2)

    t3, k3 = sorted_arr(n3)
    t6, k6 = reverse_sorted_arr(n3)
    t9, k9 = random_arr(n3)

    make_table((t1, k1), (t2, k2), (t3, k3), (t4, k4), (t5, k5), (t6, k6), (t7, k7), (t8, k8), (t9, k9))


main()
