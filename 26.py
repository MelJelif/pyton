def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
        
num = int(input("Введите число: "))
dgr = int(input("Введите степень числа: "))

print(power(num, dgr))
