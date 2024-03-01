# Написать программу для выполнения некоторых операций с текстом. Вводить текст не
# требуется, он должен быть задан в исходном тексте программы в виде списка строк
# (при выводе на экран каждый элемент этого списка должен начинаться с новой
# строки). В качестве текста в программе следует указать фрагмент литературного
# произведения из 5-7 предложений, который разбить на 7-10 строк.
# Программа должна позволять с помощью меню выполнить следующие действия:
# 1. Выровнять текст по левому краю.
# 2. Выровнять текст по правому краю.
# 3. Выровнять текст по ширине.
# 4. Удаление всех вхождений заданного слова.
# 5. Замена одного слова другим во всём тексте.
# 6. Вычисление арифметических выражений над целыми числами внутри текста (сложение и вычитание).
# 7. Найти (вывести на экран) и затем удалить слово или предложение по варианту. Предложение с самым коротким словом
# Текст следует разбить по строкам так, чтобы предложения не заканчивались в концах
# строк (никакая строка, кроме последней, не должна оканчиваться точкой).

text = [
    "Текст (от лат textus ткань; сплетение, сочетание, 2+2-3  зафиксированная на -2+4 каком-либо материальном носителе",
    "человеческая мысль; вобщем плане связная  полная последовательность символов. Существуют две основные трактовки",
    "понятия «текст»: имманентная (расширенная, философски нагруженная) и репрезентативная (более частная). Имманентный "
    "подход подразумевает отношение к тексту как к автономной реальности, нацеленность на выявление его",
    "внутренней структуры. Репрезентативный — рассмотрение текста как особой формы представления информации о внешней",
    "тексту действительности. В лингвистике термин «текст» используется в широком значении, включая и образцы"
    " устной речи. Восприятие текста изучается в рамках лингвистики текста и психолингвистики. Так, например, Гальперин определяет",
    "текст следующим образом: Это письменное сообщение, объективированное в виде письменного документа, состоящее из",
    "ряда высказываний, объединённых разными типами лексической, грамматической и логической связи, имеющее",
    "определённый модальный характер, прагматическую установку и соответственно литературно обработанное."]


def max_string_len(text):
    return len(max([string for string in text], key=len))


def align_left(text):
    max_str = max_string_len(text)
    raw_text = [s.strip() for s in text]
    # res = [s + ' ' * (max_str - len(s)) for s in raw_text]
    res = [' '.join(string.split()).ljust(max_string_len(text), ' ') for string in raw_text]
    return res


def align_right(text):
    max_str = max_string_len(text)
    raw_text = [s.strip() for s in text]
    # res = [' ' * (max_str - len(s)) + s for s in raw_text]
    res = [' '.join(string.split()).rjust(max_string_len(text), ' ') for string in raw_text]
    return res


def align_width(text):
    text = [s.strip() for s in text]
    max_string = max_string_len(text)
    res = []
    for string in text:
        words = string.split()
        need_spaces = (max_string - len(string)) + string.count(' ')
        spaces = [need_spaces // (len(words) - 1)] * (len(words) - 1)
        spaces[-1] += need_spaces % (len(words) - 1)
        while max(spaces) - min(spaces) > 1:
            spaces[spaces.index(min(spaces))] += 1
            spaces[spaces.index(max(spaces))] -= 1
        res_str = ''
        for i in range(len(words) - 1):
            res_str += words[i] + ' ' * spaces[i]
        res_str += words[-1]
        res.append(res_str)

    return res


def delete_word(text):
    word = None
    while word is None:
        try:
            word = input('Введите слово которое хотите удалить: ')
            for i in word.split('-'):
                if not i.isalpha():
                    word = None
                    raise Exception()
        except Exception:
            print('Слово это набор букв без пробелов, цифр и других символов')
    for i in range(len(text)):
        tmp = text[i].split()
        for j in range(len(tmp)):
            if tmp[j].lower() == word.lower():
                tmp[j] = ''
            if tmp[j][:-1].lower() == word.lower() and tmp[j][-1] in '.,?!:;«»':
                tmp[j] = tmp[j][-1]
            if tmp[j][1:-1].lower() == word.lower() and tmp[j][0] in '"«' and tmp[j][-1] in '"»':
                tmp[j] = ''
            if tmp[j][1:-2].lower() == word.lower() and tmp[j][0] in '"«' and tmp[j][-2] in '"»' and tmp[j][
                -1] in '.,?!:;':
                tmp[j] = tmp[j][-1]
        text[i] = ' '.join(tmp)
    return text


def replace_words(text):
    word1 = None
    # while word1 is None:
    #     try:
    word1 = input('Введите слово которое хотите заменить: ')
    #     for i in word1.split('-'):
    #         if not i.isalpha():
    #             word1 = None
    #             raise Exception()
    # except Exception:
    #     print('Слово это набор букв без пробелов и цифр и других символов')

    # word2 = None
    # while word2 is None:
    #     try:
    word2 = input('Введите слово на которое хотите заменить: ')
    #     for i in word2.split('-'):
    #         if not i.isalpha():
    #             word2 = None
    #             raise Exception()
    # except Exception:
    #     print('Слово это набор букв без пробелов, цифр и других символов')
    for i in range(len(text)):
        tmp = text[i].split()
        for j in range(len(tmp)):
            if tmp[j].lower() == word1.lower():
                tmp[j] = word2
            if tmp[j][:-1].lower() == word1.lower() and tmp[j][-1] in '.,?!:;«»':
                tmp[j] = word2 + tmp[j][-1]
            if tmp[j][1:-1].lower() == word1.lower() and tmp[j][0] in '"«' and tmp[j][-1] in '"»':
                tmp[j] = tmp[j][0] + word2 + tmp[j][-1]
            if tmp[j][1:-2].lower() == word1.lower() and tmp[j][0] in '"«' and tmp[j][-2] in '"»' and tmp[j][
                -1] in '.,?!:;':
                tmp[j] = tmp[j][0] + word2 + tmp[j][-2:]
        text[i] = ' '.join(tmp)
    return text


def calculation_arithmetic_expressions(text):
    for i in range(len(text)):
        cursor_pos = 0
        while cursor_pos < len(text[i]):
            if text[i][cursor_pos] in '+-':
                left_arg = ''
                min_k = cursor_pos
                for k in range(cursor_pos - 1, -1, -1):
                    if text[i][k] == ' ':
                        break
                    if text[i][k] == '-':
                        if not left_arg:
                            break
                        else:
                            left_arg = text[i][k] + left_arg
                            min_k = k
                            continue
                    if text[i][k] in '0123456789' and '-' not in left_arg:
                        left_arg = text[i][k] + left_arg
                    else:
                        break
                    min_k = k
                if not left_arg:
                    cursor_pos += 1
                    continue
                max_k = cursor_pos
                right_arg = ''
                for k in range(cursor_pos + 1, len(text[i])):
                    if text[i][k] == ' ':
                        continue
                    if not text[i][k].isdigit():
                        break
                    if text[i][k] == '-':
                        if right_arg == '':
                            right_arg = text[i][k] + right_arg
                            max_k = k
                            continue
                    if text[i][k] in '0123456789':
                        right_arg += text[i][k]
                    else:
                        break
                    max_k += 1
                if not right_arg:
                    cursor_pos += 1
                    continue
                if text[i][cursor_pos] == '+':
                    result = str(int(left_arg) + int(right_arg))
                else:
                    result = str(int(left_arg) - int(right_arg))
                text[i] = text[i][:min_k] + result + text[i][max_k + 1:]
                cursor_pos = min_k
            cursor_pos += 1
    return text


def delete_sentence_with_shortest_word(text):
    text = align_left(text)
    sentences_pos = []
    for i in range(len(text)):
        start_ind = 0
        while True:
            tmp = text[i].find('.', start_ind)
            if tmp == -1:
                break
            else:
                if len(sentences_pos) == 0:
                    sentences_pos.append([[0, 0], [i, tmp]])
                else:
                    t_str = sentences_pos[-1][1][0]
                    t_pos = sentences_pos[-1][1][1]
                    while True:
                        try:
                            t_pos += 1
                            if len(text[t_str]) == t_pos:
                                t_str += 1
                                t_pos = 0
                            if text[t_str][t_pos] != '.' and text[t_str][t_pos] != ' ':
                                break
                        except:
                            break

                    sentences_pos.append([[t_str, t_pos], [i, tmp]])
                start_ind = tmp + 1

    need_sent_id = -1
    removable_sent = ''
    len_min_word = None
    for i in range(len(sentences_pos)):
        tmp = ''
        if sentences_pos[i][1][0] == sentences_pos[i][0][0]:
            tmp = text[sentences_pos[i][1][0]][sentences_pos[i][0][1]:sentences_pos[i][1][1]]
        else:
            for j in range(sentences_pos[i][0][0], sentences_pos[i][1][0] + 1):
                if j == sentences_pos[i][1][0]:
                    tmp += ' ' + text[j][:sentences_pos[i][1][1] + 1] + ' '
                elif j == sentences_pos[i][0][0]:
                    tmp += ' ' + text[j][sentences_pos[i][0][1]:] + ' '
                else:
                    tmp += ' ' + text[j] + ' '
        tmp = tmp.split()
        for word in tmp:
            if len_min_word is None or (len(word) < len(len_min_word)):
                len_min_word = word
                need_sent_id = i
                removable_sent = ' '.join(tmp)
    if need_sent_id != -1:
        if sentences_pos[need_sent_id][0][0] == sentences_pos[need_sent_id][1][0]:
            text[sentences_pos[need_sent_id][0][0]] = \
                text[sentences_pos[need_sent_id][0][0]
                ][:sentences_pos[need_sent_id][0][1]] + \
                text[sentences_pos[need_sent_id][0][0]
                ][sentences_pos[need_sent_id][1][1] + 1:]

        else:
            text[sentences_pos[need_sent_id][0][0]] = \
                text[sentences_pos[need_sent_id][0]
                [0]][:sentences_pos[need_sent_id][0][1]]

            text[sentences_pos[need_sent_id][1][0]] = \
                text[sentences_pos[need_sent_id][1]
                [0]][sentences_pos[need_sent_id][1][1] + 1:]

            for k in range(sentences_pos[need_sent_id][1][0] - 1,
                           sentences_pos[need_sent_id][0][0], -1):
                text.pop(k)

    try:
        while text.index('') != -1:
            text.pop(text.index(''))
    except Exception:
        pass
    print('-' * 50)
    if removable_sent != '':
        print('Удаляемое предложение:')
        print(removable_sent)
    else:
        print('Такое предложение не найдено!')
    print('-' * 50)
    return align_left(text)


def finish_program(text):
    print('Программа завершена!')
    exit()


def print_text(text):
    if len(text) == 0:
        print('Вы удалили весь текст!')
        finish_program(text)
    else:
        print(*text, sep='\n')


def function_select(number):
    if number == 1:
        return align_left
    elif number == 2:
        return align_right
    elif number == 3:
        return align_width
    elif number == 4:
        return delete_word
    elif number == 5:
        return replace_words
    elif number == 6:
        return calculation_arithmetic_expressions
    elif number == 7:
        return delete_sentence_with_shortest_word
    elif number == 0:
        return finish_program


def menu_generator():
    menu_items = [
        'Меню:',
        '1. Выровнять текст по левому краю.',
        '2. Выровнять текст по правому краю.',
        '3. Выровнять текст по ширине.',
        '4. Удаление всех вхождений заданного слова.',
        '5. Замена одного слова другим во всём тексте.',
        '6. Вычисление арифметических выражений над целыми числами внутри текста '
        '(умножение и деление).',
        '7. Найти (вывести на экран) и затем удалить предложение с cамым коротким словом.',
        '0. Завершить программу',
    ]
    print(*menu_items, sep='\n')

    item_selected_number = None
    while item_selected_number is None:
        try:
            item_selected_number = int(
                input('Введите номер операции которую хотите выполнить: '))
            if not (0 <= item_selected_number <= 7):
                item_selected_number = None
                raise ValueError()
        except ValueError:
            print('Номер операции должен быть числом от 0 до 7')

    return function_select(item_selected_number)


def main():
    global text
    print_text(text)
    while True:
        print('-' * 50)
        func = menu_generator()
        print('-' * 50)
        text = func(text)
        print_text(text)


main()
