while True:
    x = input('Введите значение выручки \n')
    if x.isdigit():
        x = int (x)
        break
while True:
    y = input('Введите значение издержки \n')
    if y.isdigit():
        y = int (y)
        break
if x>y:
    ren = (x-y) / x
    while True:
        z = input('Введите количество сотрудников \n')
        if z.isdigit():
            z = int(z)
            break
    val = (x-y) / z
    print(ren)
    print(val)