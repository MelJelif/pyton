import random

Num = int(input("Введите размер: "))
Arr = [random.randint(-100, 100) for i in range(Num)] #заполнение массива
x = int(input("Искомое число: ")) #иск как мистер икс неизвестное.
closest_num = None
closest_diff = None
print(Arr) #вывод массива

#перебор с наимеьшей поиском разницы
for num in Arr:
    diff = abs(num - x)
    if closest_diff is None or diff < closest_diff:
        closest_diff = diff
        closest_num = num

print("Ближайшее число к", x, ":", closest_num)