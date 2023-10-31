# Павлов Д. В. ИУ7-13Б
# Поиск элемента наибольшей длины, не содержащего английских гласных

# Блок ввода
s = list(map(str, input("Введите элементы списка в одну строку через пробел: ").split()))  # формирование списка
n = len(s)

vowels = 'eyuioa'  # гласные в английском алфавите
s_max = ''

# Блок вычисления
for elem in s:
    is_vowel_in_elem = False
    for letter in elem:
        if letter in vowels:
            is_vowel_in_elem = True
            break
    if not is_vowel_in_elem:
        s_max = max(elem, s_max, key=len)

    # if not any([i in elem for i in vowels]):
    #     s_max = max(elem, s_max, key=len)

if s_max:
    print(f"Наибольший элемент не содержащий английскую гласную: {s_max}")
else:
    print("Не удалось найти требуемый элемент")
