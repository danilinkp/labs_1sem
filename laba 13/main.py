import os.path


def is_name_correct(name: str) -> bool:
    for i in ',.<>:\'"/?|*':
        if i in name:
            return False
    return True


def is_correct_name_of_file(file_name: str) -> bool:
    file_attributes = file_name.split('.')
    if len(file_attributes) != 2 or file_attributes[-1] != 'txt':
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
        file = open(file_name, 'r')
    except Exception:
        return False
    return True


def file_selection():
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
    path = name.split('/')
    path = '/'.join(path[:-1])
    if not os.path.isdir(path) and len(path) > 1:
        os.makedirs(path)
    if lines is None:
        lines = ''
    with open(file=name, mode='w') as f:
        f.write('; '.join(['Имя артиста', 'Название альбома', 'Год выпуска альбома']) + '\n')
        for line in lines:
            f.write(line + '\n')


def make_line(db_name):
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

    line = '; '.join([name_of_songer, name_of_album, str(year_of_release)])
    return line


def db_initialization():
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
            print('Название файла должно иметь ввид file.txt\nИ в названии файла не должны быть символы ,.<>:\'"/?|*\\')
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
                print("Ответ должен быть целым числом от 1 до 2")
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
        # db_create(db_name, [make_field()])
        db_create(db_name, [make_line(db_name) for i in range(lines_count)])
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
        # db_create(db_name, [make_field()])
        db_create(db_name, [make_line(db_name) for i in range(lines_count)])
    return db_name


def show_db(db_name):
    with open(file=db_name, mode='r') as f:
        print('-' * 71)
        for row in f.readlines():
            data = row.replace('\n', '').split(';')
            print('| {:^20} | {:^20} | {:^20} |'.format(*data))
            print('-' * 71)


def add_line(db_name, line):
    with open(file=db_name, mode='a') as f:
        f.write(line + '\n')


def add_line_in_db(db_name):
    add_line(db_name, make_line(db_name))


def search_by_name_of_songer(db_name, songer):
    founded_lines = []
    with open(file=db_name, mode='r') as f:
        for line in f.readlines()[1:]:
            if not line:
                break
            tmp_line = line.split(';')
            if tmp_line[0] == songer:
                founded_lines.append(line.split(';'))
    return founded_lines


def search_by_name_of_album_and_year_of_realize(db_name, album, year):
    founded_lines = []
    with open(file=db_name, mode='r') as f:
        for line in f.readlines()[1:]:
            if not line:
                break
            tmp_line = line.split('; ')
            if tmp_line[1] == album and int(tmp_line[2].split('\n')[0]) == int(year):
                founded_lines.append(line.split(';'))
    return founded_lines


def search_album_and_year_cols(db_name):
    album = input('Введите название альбома: ')
    year = None
    while year is None:
        try:
            year = int(input('Введите год выхода альбома: '))
        except:
            print("Год должен быть целым числом")
    res = search_by_name_of_album_and_year_of_realize(db_name, album, year)

    if len(res) == 0:
        print('Строка с заданным названием и годом не найдены')
    else:
        head = ['Имя артиста', 'Название альбома', 'Год выпуска альбома']
        print('| {:^20} | {:^20} | {:^20} |'.format(*head))
        for data in res:
            print('| {:^20} | {:^20} | {:^20} |'.format(*data[:-1] + data[-1].split('\n')))
            print('-' * 71)


def search_songer(db_name):
    songer = input("Введите имя артиста: ")
    res = search_by_name_of_songer(db_name, songer)
    if len(res) == 0:
        print('Строка с заданным именем не найдена')
    else:
        head = ['Имя артиста', 'Название альбома', 'Год выпуска альбома']
        print('| {:^20} | {:^20} | {:^20} |'.format(*head))
        print('-' * 70)
        for data in res:
            print('| {:^20} | {:^20} | {:^20} |'.format(*data[:-1] + data[-1].split('\n')))
            print('-' * 70)


def finish_program():
    print('Программа завершена!')
    exit()


db_name_use = None


def menu():
    funcs = [
        finish_program,
        file_selection,
        db_initialization,
        show_db,
        add_line_in_db,
        search_songer,
        search_album_and_year_cols,
    ]
    text = [
        'Меню:',
        '1) Выбрать файл для работы',
        '2) Инициализировать базу данных',
        '3) Вывести содержимое базы данных',
        '4) Добавить запись в конец базы данных',
        '5) Поиск по одному полю (songer)',
        '6) Поиск по двум полям (album, yaer)',
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
            if not (0 <= item_selected_number < 7):
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
        db_name_use = funcs[1]()
    elif item_selected_number == 2:
        db_name_use = funcs[2]()
    else:
        print('-' * 50)
        if db_name_use is None:
            print('Ошибка выберите сначала бд с которой будете работать (пункт 1 или 2)')
        else:
            funcs[item_selected_number](db_name_use)


while True:
    menu()
