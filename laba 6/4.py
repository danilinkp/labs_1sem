# Найти наиболее длинную непрерывную последовательность 8. Знакочередующаяся последовательность чётных чисел.

# Блок ввода списка
s = list(map(int, input("Введите элементы списка в одну строку через пробел: ").split()))  # формирование списка
n = len(s)

even_sequence = []  # текущая последовательность
longest_sequence = []  # наибольшая последовательность

# Блок нахождения длинейшей последовательности
for i in range(n):
    if s[i] % 2 == 0 and len(even_sequence) == 0:
        even_sequence.append(s[i])
    elif s[i] % 2 == 0 and even_sequence[-1] * s[i] < 0:
        even_sequence.append(s[i])
        longest_sequence = max(even_sequence, longest_sequence, key=len)
    elif s[i] % 2 == 0 and even_sequence[-1] * s[i] > 0:
        even_sequence = [s[i]]
    else:
        even_sequence = []

# Блок вывода
if longest_sequence:
    print(
        f"Наиболее длинная последовательность1: {' '.join(map(str, longest_sequence))}"
    )
else:
    print("Нету такой последовательности")
