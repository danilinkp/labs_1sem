# Павлов Д. В. ИУ7-13Б
#
# Требуется написать программу, которая позволит с помощью меню выполнить
# следующие действия:
# 1. Выбрать файл для работы
# 2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
# его записями)
# 3. Вывести содержимое базы данных
# 4. Добавить запись в произвольное место базы данных (пользователь указывает
# номер позиции, в которую должна быть вставлена запись)
# 5. Удалить произвольную запись из базы данных (пользователь указывает номер
# удаляемой записи)
# 6. Поиск по одному полю (Имя артиста)
# 7. Поиск по двум полям (2 и 3)

# Тематика: 1. Имя артиста 2. Название альбома 3. Год выпуска альбома


import struct
import os.path

DB_FORMAT = '20s20si'


def is_name_correct(name):
    """Проверка на правильность имени каталогов файла"""
    for i in ',.<>:\'"/?|*':
        if i in name:
            return False
    return True


def is_correct_name_of_file(file_name):
    """Проверка на правильность имени файла"""
    file_attributes = file_name.split('.')
    if len(file_attributes) != 2 or file_attributes[-1] not in ['txt', 'bin']:
        return False
    if not is_name_correct(file_attributes[0]) or not is_name_correct(file_attributes[1]):
        return False
    return True


def is_correct_path(file_path):
    """Проверка на правильность пути файла"""
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
    """Проверка на существование файла"""
    try:
        file = open(file_name, 'r')
        file.close()
    except Exception:
        return False
    return True


def file_selection(DB_FORMAT):
    """Функция выбора файла"""
    db_name = None
    while db_name is None:
        try:
            db_name = input("Введите название файла (разделитель /): ")
            if not is_correct_path(db_name):
                db_name = None
                raise ValueError
            if not check_file_is_exists(db_name):
                db_name = None
                raise FileNotFoundError
        except ValueError:
            print('Название файла должно иметь ввид file.txt\nИ в названии файла не должны быть символы ,.<>:\'"/?|*\\')
        except FileNotFoundError:
            print("Такого файла не существует")
    return db_name


def db_create(name, lines):
    """Функция создания бд"""
    path = name.split('/')
    path = '/'.join(path[:-1])
    if not os.path.isdir(path) and len(path) > 1:
        os.makedirs(path)
    if lines is None:
        lines = ''
    with open(file=name, mode='w+b') as f:
        for line in lines:
            f.write(line)


def make_line(db_name, DB_FORMAT):
    """Функция создания строки бд"""
    name_of_songer = name_of_album = year_of_release = None
    while name_of_songer is None:
        try:
            name_of_songer = input("Введите имя артиста которого вы хотите добавить: ")
            if len(name_of_songer) < 0:
                name_of_songer = None
                raise ValueError
        except ValueError:
            print("Имя артиста не может быть пустой строкой")
    while name_of_album is None:
        try:
            name_of_album = input("Введите название альбома которого вы хотите добавить: ")
            if len(name_of_album) < 0:
                name_of_album = None
                raise ValueError
        except ValueError:
            print("Имя альбома не может быть пустой строкой")
    while year_of_release is None:
        try:
            year_of_release = int(input("Введите год выпуска альбома: "))
            if year_of_release < 0:
                year_of_release = None
                raise ValueError
        except ValueError:
            print("Год выхода должен быть целым числом больше нуля")

    line = [name_of_songer.encode(), name_of_album.encode(), int(year_of_release)]
    structed_line = struct.pack(DB_FORMAT, *line)
    return structed_line


def db_initialization(DB_FORMAT):
    """Инициализация бд(создание)"""
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
                'Название файла должно иметь ввид file.txt или file.bin\nИ в названии файла не должны быть символы ,.<>:\'"/?|*\\')
        except FileNotFoundError:
            print("Такого файла не существует")
            print("Но вы можете его создать")

    if check_file_is_exists(db_name):
        print("Этот файл существует, хотите ли вы его перезаписать?")
        answer = None
        while answer is None:
            try:
                answer = int(input("Введите номер варианта ответа: 1 - перезаписать, 0 - не перезаписывать: "))
                if not (0 <= answer <= 1):
                    answer = None
                    raise Exception
            except Exception:
                print("Ответ должен быть целым числом от 0 до 1")
        if answer == 0:
            return db_name
        lines_count = None
        while lines_count is None:
            try:
                lines_count = int(input("Введите количество записей, которые хотите создать при инициализации: "))
                if lines_count < 0:
                    lines_count = None
                    raise ValueError
            except ValueError:
                print("Кол-во записей должно быть целым числом больше или равное 0")
        db_create(db_name, [make_line(db_name, DB_FORMAT) for i in range(lines_count)])
    else:
        lines_count = None
        while lines_count is None:
            try:
                lines_count = int(input("Введите количество записей, которые хотите создать при инициализации: "))
                if lines_count < 0:
                    lines_count = None
                    raise ValueError
            except ValueError:
                print("Кол-во записей должно быть целым числом больше или равное 0")
        db_create(db_name, [make_line(db_name, DB_FORMAT) for i in range(lines_count)])
    return db_name


def print_line(line, DB_FORMAT, ind):
    """Вывод строки бд"""
    data = struct.unpack(DB_FORMAT, line)
    if len(data) <= 3:
        tmp = ['None'] * 3
        for i in range(len(data)):
            try:
                tmp[i] = data[i].rstrip(b'\x00').decode()
            except:
                tmp[i] = data[i]
        data = tmp
    print('| {:^25} | {:^25} | {:^25} |'.format(*data))


def get_db_line_count(db_path, DB_FORMAT):
    """Подсчёт кол-ва строк в бд"""
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(db_path, 'rb') as f:
        try:
            f.seek(0, os.SEEK_END)
            size = f.tell()
        except OSError:
            f.seek(0)
            size = f.tell()
    return size // LINE_SIZE


def show_db(db_path, DB_FORMAT):
    """Вывод БД"""
    lines_count = get_db_line_count(db_path, DB_FORMAT)
    if lines_count == 0:
        print('База данных пустая')
        return
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    tmp = '| {:^25} | {:^25} | {:^25} |'.format("Имя артиста", "Название альбома", "Год выпуска альбома")
    width = len(tmp)
    print('-' * width)
    print(tmp)
    print('|' + '-' * (width - 2) + '|')
    ind = 1
    with open(db_path, 'rb') as f:
        while True:
            line = f.read(LINE_SIZE)
            if not line:
                break
            print_line(line, DB_FORMAT, ind)
            ind += 1

    print('-' * width)


def line_add(db_path, DB_FORMAT, line_index, lines_count, new_line):
    """Добавление строки"""
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(db_path, 'r+b') as f:
        try:
            f.seek(-LINE_SIZE, os.SEEK_END)
            while lines_count > line_index - 1:
                prev_chunk = f.read(LINE_SIZE)
                f.write(prev_chunk)
                if line_index == 1:
                    if lines_count - line_index != 0:
                        f.seek(-LINE_SIZE * 3, os.SEEK_CUR)
                    else:
                        f.seek(0)
                else:
                    f.seek(-LINE_SIZE * 3, os.SEEK_CUR)
                lines_count -= 1
        except:
            pass
        if lines_count == 0:
            f.seek(0)
        elif line_index != 1:
            f.seek(LINE_SIZE, os.SEEK_CUR)
        f.write(new_line)


def add_line_in_db(db_path, DB_FORMAT):
    """Добавление строки в БД"""
    lines_count = get_db_line_count(db_path, DB_FORMAT)
    # if lines_count == 0:
    tmp = lines_count + 1
    # else:
    #     tmp = lines_count
    line_index = None
    while line_index is None:
        try:
            line_index = int(
                input(f"Введите номер строки куда хотите вставить (строки под сдвинутся вниз) (от 1 до {tmp}): "))
            if not 0 < line_index <= tmp:
                raise Exception
        except Exception:
            print(f"Номер строки должен быть целым числом и меньше или равен {tmp}")
    new_line = make_line(db_path, DB_FORMAT)
    line_add(db_path, DB_FORMAT, line_index, lines_count, new_line)


def line_remove(db_path, DB_FORMAT, line_index):
    """Удаление строки"""
    LINE_SIZE = struct.calcsize(DB_FORMAT)
    with open(db_path, "r+b") as f:
        f.seek(LINE_SIZE * line_index)
        while True:
            line = f.read(LINE_SIZE)
            if not line:
                break
            f.seek(-LINE_SIZE * 2, os.SEEK_CUR)
            f.write(line)
            f.seek(LINE_SIZE, os.SEEK_CUR)

        f.truncate(os.path.getsize(db_path) - LINE_SIZE)


def del_line_from_db(db_path, DB_FORMAT):
    """Удаление строки из БД"""
    lines_count = get_db_line_count(db_path, DB_FORMAT)
    if lines_count == 0:
        print('База данных пустая')
        return
    line_index = None
    while line_index is None:
        try:
            line_index = int(
                input(f"Введите номер строки которую хотите удалить (от 1 до {lines_count}): "))
            if not 0 < line_index <= lines_count:
                raise Exception
        except Exception:
            print("Номер строки должен быть положительным целым числом")
    line_remove(db_path, DB_FORMAT, line_index)


def search_by_name_of_songer(db_name, DB_FORMAT, songer):
    """Поиск по имени артитса"""
    flag = False
    ind = 1
    with open(db_name, 'rb') as f:
        while True:
            LINE_SIZE = struct.calcsize(DB_FORMAT)
            line = f.read(LINE_SIZE)
            if not line:
                break
            line_data = struct.unpack(DB_FORMAT, line)
            try:
                tmp = line_data[0].rstrip(b'\x00').decode()
            except:
                tmp = line_data[0]
            if tmp == songer:
                if not flag:
                    tmp = '| {:^25} | {:^25} | {:^25} |' \
                        .format("Имя артиста", "Название альбома", "Год выпуска")
                    width = len(tmp)
                    print('-' * width)
                    print(tmp)
                    print('|' + '-' * (width - 2) + '|')
                    flag = True
                print_line(line, DB_FORMAT, ind)
                ind += 1
    if flag:
        print('-' * width)
    return ind


def search_by_name_of_album_and_year_of_realize(db_name, DB_FORMAT, album, year):
    """Поиск по альбому и году его выпуска"""
    flag = False
    ind = 1
    with open(db_name, 'rb') as f:
        while True:
            LINE_SIZE = struct.calcsize(DB_FORMAT)
            line = f.read(LINE_SIZE)
            if not line:
                break
            line_data = struct.unpack(DB_FORMAT, line)
            try:
                tmp_album = line_data[1].rstrip(b'\x00').decode()
                tmp_year = line_data[2]
            except:
                tmp_album = line_data[1]
                tmp_year = line_data[2]
            if int(tmp_year) == year and tmp_album == album:
                if not flag:
                    tmp = '| {:^25} | {:^25} | {:^25} |' \
                        .format("Имя артиста", "Название альбома", "Год выпуска")
                    width = len(tmp)
                    print('-' * width)
                    print(tmp)
                    print('|' + '-' * (width - 2) + '|')
                    flag = True
                print_line(line, DB_FORMAT, ind)
                ind += 1
    if flag:
        print('-' * width)
    return ind


def search_songer(db_name, DB_FORMAT):
    """Поиск артиста"""
    songer = input("Введите имя артиста: ")
    res = search_by_name_of_songer(db_name, DB_FORMAT, songer)
    if res - 1 == 0:
        print('Строка с заданным именем не найдена')


def search_album_and_year_cols(db_name, DB_FORMAT):
    """Поиск альбома и года"""
    album = input('Введите название альбома: ')
    year = None
    while year is None:
        try:
            year = int(input('Введите год выхода альбома: '))
        except:
            print("Год должен быть целым числом")
    res = search_by_name_of_album_and_year_of_realize(db_name, DB_FORMAT, album, year)

    if res - 1 == 0:
        print('Строка с заданным названием и годом не найдены')
    else:
        res = search_by_name_of_album_and_year_of_realize(db_name, DB_FORMAT, album, year)


def finish_program():
    """Завершение прогшраммы"""
    print('Программа завершена!')
    exit()


db_name_use = None


def menu():
    """Меню"""
    funcs = [
        finish_program,
        file_selection,
        db_initialization,
        show_db,
        add_line_in_db,
        del_line_from_db,
        search_songer,
        search_album_and_year_cols,
    ]
    text = [
        'Меню:',
        '1) Выбрать файл для работы',
        '2) Инициализировать базу данных',
        '3) Вывести содержимое базы данных',
        '4) Добавить запись в произвольное место базы данных',
        '5) Удалить произвольную запись из базы данных',
        '6) Поиск по одному полю (songer)',
        '7) Поиск по двум полям (album, yaer)',
        '0) Завершить программу',
    ]
    print('-' * 50)
    print(*text, sep='\n')
    print('-' * 50)
    item_selected_number = None
    while item_selected_number is None:
        try:
            item_selected_number = int(
                input('Введите номер операции которую хотите выполнить: '))
            if not (0 <= item_selected_number <= 7):
                item_selected_number = None
                raise ValueError()
        except ValueError:
            print('-' * 50)
            print('Номер операции должен быть целым числом от 0 до 6')
            print('-' * 50)

    global db_name_use
    if item_selected_number == 0:
        funcs[0]()
    elif item_selected_number == 1:
        db_name_use = funcs[1](DB_FORMAT)
    elif item_selected_number == 2:
        db_name_use = funcs[2](DB_FORMAT)
    else:
        print('-' * 50)
        if db_name_use is None:
            print('Ошибка выберите сначала бд с которой будете работать (пункт 1 или 2)')
        else:
            funcs[item_selected_number](db_name_use, DB_FORMAT)


while True:
    menu()
