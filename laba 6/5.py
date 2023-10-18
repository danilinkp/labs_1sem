# Поменять местами элементы с характеристиками по варианту 9. Первый чётный и максимальный положительный.

# Блок ввода списка
s = list(map(int, input("Введите элементы списка в одну строку через пробел: ").split()))  # формирование списка
n = len(s)

m = -10 ** 20  # максимальное число
m_ind = 0  # индекс максимального числа
first_even = -1  # индекс первого четного

# Блок выявления индексов элементов с заданныыми характеристиками
for i in range(n - 1, -1, -1):
    if s[i] % 2 == 0:
        first_even = i
    if s[i] > m:
        m = s[i]
        m_ind = i

# Блок проверки данных и вывод
if m_ind == first_even:
    print("Ничего не поменялось")
    print(f"Полученный список: {' '.join(map(str, s))}")
elif m < 0:
    print("Наибольшего положительного в списке нет, замену сделать не удалось")
elif first_even == -1:
    print("Четных чисел нет, замену сделать не удалось")
else:
    s[m_ind], s[first_even] = s[first_even], s[m_ind]
    print(f"Полученный список: {' '.join(map(str, s))}")