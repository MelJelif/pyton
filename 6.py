number = input("Введите шестизначный номер билета: ")
if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
    print("yes")
else:
    print("no")
