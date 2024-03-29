# Yдалить элемент с заданным индексом алгоритмически.

# Блок ввода
s = list(map(int, input("Введите элементы списка в одну строку через пробел: ").split()))  # формирование списка
n = len(s)
ind = int(input("Введите индекс элемента, которого хотите удалить: "))

# Обработка ошибки
while not (0 <= ind < n):
    print('Ошибка! Индекс должнен быть в пределах размера массива')
    ind = int(input('Введите индекс(отсчет с 0) куда добавить новый элемент: '))

# Блок удаления заданного элемента
for i in range(ind + 1, n):
    s[i - 1] = s[i]
s.pop()

# Блок вывода
print(f"Полученный список: {' '.join(map(str, s))}")
