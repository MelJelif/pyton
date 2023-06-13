def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

num1 = int(input("Введите слагаемое 1: "))
num2 = int(input("Введите слагаемое 2: "))

print(sum(num1, num2))