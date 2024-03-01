# Сортировка методом расчёски

import struct
import funcs


def comb_sort(FORMAT, file_name):
    LINE_SIZE = struct.calcsize(FORMAT)
    nums_count = funcs.get_db_line_count(FORMAT, file_name)
    step = nums_count
    factor = 1.247331
    is_swapped = False
    with open(file_name, "r+b") as f:
        while step > 1 or is_swapped:
            if step > 1:
                step = int(step / factor)
            is_swapped = False
            i = 0
            while (i + step) < nums_count:
                f.seek(LINE_SIZE * i)
                num_i_bin = f.read(LINE_SIZE)
                num_i = struct.unpack(FORMAT, num_i_bin)[0]
                f.seek(LINE_SIZE * (i + step))
                num_i_step_bin = f.read(LINE_SIZE)
                num_i_step = struct.unpack(FORMAT, num_i_step_bin)[0]
                if num_i > num_i_step:
                    f.seek(LINE_SIZE * i)
                    f.write(num_i_step_bin)
                    f.seek(LINE_SIZE * (i + step))
                    f.write(num_i_bin)
                    is_swapped = True
                i += step


FORMAT = 'l'
file_name = funcs.file_selection(FORMAT)

funcs.add_nums(FORMAT, file_name)

comb_sort(FORMAT, file_name)

funcs.print_nums(FORMAT, file_name)
