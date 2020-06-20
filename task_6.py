while True:
    a = input("Введите число результата в 1 день\n")
    if a.isdigit():
        a = int (a)
        break
while True:
    b = input("Введите желаемый результат \n")
    if b.isdigit():
        b = int (b)
        break
day = 1
tmp = a
while tmp <= b:
    tmp *= 1.1
    day +=1
print(day)