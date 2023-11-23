# Павлов Д. В. ИУ7-13б

# Меиод "Расчёсок"
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
            array = list(map(int, input("Введите массив целочисленных чисел: ").split()))
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
    arr = [i for i in range(1, n + 1)]
    start_time = time.time()
    permutations = comb_sort(arr)
    end_time = time.time()
    total_time = end_time - start_time
    return permutations, total_time


def reverse_sorted_arr(n: int) -> tuple:
    arr = [i for i in range(n, 0, -1)]
    start_time = time.time()
    permutations = comb_sort(arr)
    end_time = time.time()
    total_time = end_time - start_time
    return permutations, total_time


def random_arr(n: int) -> tuple:
    arr = [randint(-100000, 100000) for i in range(n)]
    start_time = time.time()
    permutations = comb_sort(arr)
    end_time = time.time()
    total_time = end_time - start_time
    return permutations, total_time


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

