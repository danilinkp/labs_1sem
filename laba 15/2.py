# 2. После каждого числа, имеющего свойство по варианту, добавить его удвоенное
# значение (допускается два прохода по файлу). Положительные элементы

import os
import struct
import funcs


def add_double_value(FORMAT, file_name):
    """Функция добавления удвоенных значений положительных чисел"""
    LINE_SIZE = struct.calcsize(FORMAT)
    nums_count = funcs.get_db_line_count(FORMAT, file_name)
    count = 0
    with open(file_name, "r+b") as f:
        for i in range(nums_count):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack(FORMAT, num_bin)[0]
            if num > 0:
                count += 1
        for i in range(count):
            f.seek(0, os.SEEK_END)
            f.write(struct.pack(FORMAT, 0))
    with open(file_name, "r+b") as f:
        end_ind = nums_count - 1 + count
        for i in range(nums_count - 1, -1, -1):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack(FORMAT, num_bin)[0]
            if num > 0:
                f.seek(LINE_SIZE * end_ind)
                f.write(struct.pack(FORMAT, num * 2))
                f.seek((LINE_SIZE * (end_ind - 1)))
                f.write(struct.pack(FORMAT, num))
                end_ind -= 2
            else:
                f.seek(LINE_SIZE * end_ind)
                f.write(struct.pack(FORMAT, num))
                end_ind -= 1


# Формат файла
FORMAT = 'l'

# Выбор файла
file_name = funcs.file_selection(FORMAT)


funcs.add_nums(FORMAT, file_name)

add_double_value(FORMAT, file_name)

funcs.print_nums(FORMAT, file_name)
