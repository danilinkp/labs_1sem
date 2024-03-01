text = [
    "Текст (от лат textus кан; сплетение, сочетание),зафиксированная на каком-либо материальном носителе",
    "человеческая мысль; вобщем плане связная  полная последовательность символов. Существуют две основные трактовки",
    "понятия «текст»: имманентная (расширенная, философски нагруженная) и репрезентативная (более частная). Имманентный "
    "подход подразумевает отношение к тексту как к автономной реальности, нацеленность на выявление его",
    "внутренней структуры. Репрезентативный — рассмотрение текста как особой формы представления информации о внешней",
    "тексту действительности. В лингвистике термин «текст» используется в широком значении, включая и образцы"
    "устной речи. Восприятие текста изучается в рамках лингвистики текста и психолингвистики. Так например, Гальперин определяет",
    "текст следующим образом: письменное сообщение, объективированное в виде письменного документа, состоящее из",
    "ряда высказываний, объединённых разными типами лексической, грамматической и логической связи, имеющее",
    "определённый модальный характер, прагматическую установку и соответственно литературно обработанное."]


def delete_sentence_with_max_alternating_letters(text):
    sentences_pos = []
    vowels = 'euioaуеыаоэяию'
    consonants = 'qwrtpsdfghjklzxcvbnmйцкнгшщзхъфвпрлджчсмтьб'
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
    max_count = 0
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
        tmp_count = 0
        for word in tmp:
            word = word.lower()
            is_alternating = False
            for j in range(len(word) - 1):
                if (word[j] in vowels and word[j + 1] in consonants) or (
                        word[j] in consonants and word[j + 1] in vowels):
                    is_alternating = True
                else:
                    is_alternating = False
                    break
            if is_alternating:
                tmp_count += 1
                print(word)
        print(tmp_count)
        print()
        if tmp_count > max_count:
            max_count = tmp_count
            need_sent_id = i
            removable_sent = ' '.join(tmp)
        if need_sent_id == -1 or max_count == 0:
            removable_sent = ''
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
    return text


def print_text(text):
    print(*text, sep='\n')


print_text(text)
delete_sentence_with_max_alternating_letters(text)
print_text(text)
