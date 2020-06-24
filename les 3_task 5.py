def my_func (str_value = input().split()):
    print(type(str_value))
    res = 0
    for el in str_value:
        el = int(el)
        res += el
    return res

com = input()
f = 0
while True:
    if com != 'q':
        com = com.split()
        total = my_func(com)
        f = f + total
        print(f'Сумма чисел {f}')
        com = input('Введите число (остановить "q":')
    else:
        print(f'Финиш, сумма {f}')
        break