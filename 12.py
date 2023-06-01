#запрос ввода S и P с последующей инициализацией переменных
S = int(input())
P = int(input())

#перебор всех возможных значений X и Y, определение X+Y и X*Y
#сравнение с заданными S и P
for X in range(1, 1001):
    for Y in range(1, 1001):
        if X + Y == S and X * Y == P:
            print(X, Y)
            exit()
