def power(num, dgr):
    if dgr == 0:
        return 1
    else:
        return num * power(num, dgr - 1)
        
num = int(input("Введите число: "))
dgr = int(input("Введите степень числа: "))

print(power(num, dgr))
