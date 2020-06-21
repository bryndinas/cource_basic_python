def my_func ():
    try:
        val_1 = input('Введите аргумент 1 \n')
        val_2 = input('Введите аргумент 2 \n')
        val_3 = input('Введите аргумент 3 \n')
        a = int(val_1),int(val_2),int(val_3)
        b = list(a)
        b.sort(reverse=True)
        c = b[0] + b[1]
        print(c)
    except ValueError:
        print('Введите числовые значения')

a = print(my_func())