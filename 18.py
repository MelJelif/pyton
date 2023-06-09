import random

Num = int(input("Введите размер: "))
Arr = [random.randint(1, 100) for i in range(Num)] #заполнение массива
x = int(input("Искомое число: ")) #иск как мистер икс неизвестное.
print(Arr) #вывод массива

# находим индекс элемента массива, ближайшего по модулю к x
closest_index = 0
for i in range(1, Num):
    if abs(Arr[i] - x) < abs(Arr[closest_index] - x):
        closest_index = i

print(Arr[closest_index])
