import os
import struct


def is_name_correct(name):
    for i in ',.<>:\'"/?|*':
        if i in name:
            return False
    return True


def is_correct_name_of_file(file_name):
    file_attributes = file_name.split('.')
    if len(file_attributes) != 2 or file_attributes[-1] not in ['txt', 'bin']:
        return False
    if not is_name_correct(file_attributes[0]) or not is_name_correct(file_attributes[1]):
        return False
    return True


def is_correct_path(file_path):
    path = file_path.split('/')
    if len(path) == 0:
        return False
    if not is_correct_name_of_file(path[-1]):
        return False
    if path[0] == '..' or path[0] == '.':
        start = 1
    else:
        start = 0
    if len(path) > 1:
        for i in range(start, len(path) - 1):
            if not is_name_correct(path[i]):
                return False
    return True


def check_file_is_exists(file_name):
    try:
        file = open(file_name, 'rb')
        file.close()
    except Exception:
        return False
    return True


def file_selection(DB_FORMAT):
    db_name = None
    while db_name is None:
        try:
            db_name = input("Введите название файла (разделитель /): ")
            if not is_correct_path(db_name):
                db_name = None
                raise ValueError
            if not check_file_is_exists(db_name):
                raise FileNotFoundError
        except ValueError:
            print(
                'Название файла должно иметь ввид file.txt(bin)\nИ в названии файла не должны быть символы ,.<>:\'"/?|*\\')
        except FileNotFoundError:
            print("Такого файла не существует, но он будет создан")
    return db_name


# def db_create(name, lines):
#     path = name.split('/')
#     path = '/'.join(path[:-1])
#     if not os.path.isdir(path) and len(path) > 1:
#         os.makedirs(path)
#     if lines is None:
#         lines = ''
#     with open(file=name, mode='w+b') as f:
#         for line in lines:
#             f.write(line)


def get_db_line_count(FORMAT, file_name):
    LINE_SIZE = struct.calcsize(FORMAT)
    with open(file_name, 'rb') as f:
        try:
            f.seek(0, os.SEEK_END)
            size = f.tell()
        except OSError:
            f.seek(0)
            size = f.tell()
    return size // LINE_SIZE


def line_generate(FORMAT, i):
    num = None
    while num is None:
        try:
            num = int(input(f"Введите число, номер {i + 1}: "))
        except Exception:
            num = None
            print("Число должно быть целым")
    structed_line = struct.pack(FORMAT, num)
    return structed_line


def write_in_file(FORMAT, file_name, n):
    path = file_name.split('/')
    if len(path) > 1:
        path = '/'.join(path[:-1])
        try:
            if not os.path.isdir(path):
                os.makedirs(path)
        except:
            pass

    with open(file=file_name, mode='w+b') as f:
        for i in range(n):
            f.write(line_generate(FORMAT, i))


def add_nums(FORMAT, file_name):
    lines_count = None
    while lines_count is None:
        try:
            lines_count = int(input("Введите кол-во чисел которые вы хотите добавить: "))
        except ValueError:
            print("Число должно быть целым")
            lines_count = None
    write_in_file(FORMAT, file_name, lines_count)


def print_nums(FORMAT, file_name):
    lines_count = get_db_line_count(FORMAT, file_name)
    if lines_count == 0:
        print("Файл пустой")
    line_size = struct.calcsize(FORMAT)
    ind = 0
    with open(file=file_name, mode='rb') as f:
        for i in range(lines_count):
            line = f.read(line_size)
            num = struct.unpack(FORMAT, line)
            print(f"{ind + 1}-ое число: {num[0]}")
            ind += 1
