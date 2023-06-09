n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

# Заполнение первого множества
print("Введите элементы первого множества:")
for i in range(n):
    set1.add(int(input()))

# Заполнение второго множества
print("Введите элементы второго множества:")
for i in range(m):
    set2.add(int(input()))

# Поиск пересечения множеств
intersection = set1.intersection(set2)

# Сортировка результатов и вывод на экран
sorted_intersection = sorted(list(intersection))
print("Результат:")
for num in sorted_intersection:
    print(num)
