# Павлов Д. В. ИУ7-13Б
# Замена всех цифр на пробелы

# Блок ввода
s = list(map(str, input("Введите элементы списка в одну строку через пробел: ").split()))  # формирование списка
n = len(s)

is_digit_in_s = False
s_new = []

# Блок вычисления
for i in range(n):
    for j in range(len(s[i])):
        if s[i][j].isdigit():
            el = s[i].replace(s[i][j], ' ')
            s[i] = el
            is_digit_in_s = True

if not is_digit_in_s:
    print(f"Цифр нет, список не изменился ")
else:
    print(f"Полученный список: {s}")
