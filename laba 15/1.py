# 1. Удалить все числа, имеющие свойство по варианту, за один проход по файлу.
# Нечётные элементы
# Павлов Д. В.
import os
import struct
import funcs


def del_number(FORMAT, file_name):
    """Функция удаления нечетных чисел"""
    LINE_SIZE = struct.calcsize(FORMAT)
    nums_count = funcs.get_db_line_count(FORMAT, file_name)
    count = 0
    with open(file_name, "r+b") as f:
        for i in range(nums_count):
            f.seek(LINE_SIZE * i)
            num_bin = f.read(LINE_SIZE)
            num = struct.unpack(FORMAT, num_bin)[0]
            if num % 2 != 0:
                count += 1
            else:
                f.seek(LINE_SIZE * (i - count))
                f.write(num_bin)
        f.truncate(os.path.getsize(file_name) - LINE_SIZE * count)


# Формат БД
FORMAT = 'l'

# Выбор файла
file_name = funcs.file_selection(FORMAT)

# Функция добавления чисел
funcs.add_nums(FORMAT, file_name)

del_number(FORMAT, file_name)

# Функция вывода
funcs.print_nums(FORMAT, file_name)
