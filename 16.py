import random

Num = int(input("Введите размер: "))
Arr = [random.randint(1, 10) for i in range(Num)] #заполнение массива
X = int(input("Искомое число: ")) #иск как мистер икс неизвестное.
print(Arr) #вывод массива

count_X = 0
for i in range(Num):
    if Arr[i] == X:
        count_X += 1
        
print(" -> ",count_X)