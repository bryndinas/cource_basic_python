def may_func ():
    try:
        val_1 = float(input("Укажите первое число: "))
        val_2 = float(input("Укажите второе число: "))
        res = val_1 / val_2
        return res
    except ZeroDivisionError:
        print('Деление на 0')
    except ValueError:
        print('Введите число')

print(may_func())