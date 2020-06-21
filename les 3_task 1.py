def may_func ():
    try:
        val_1 = float(input("Укажите первое число: "))
        val_2 = float(input("Укажите второе число: "))
    except ValueError:
        return
    else:
        if val_1 or val_2 == 0:
           print('Деление на 0')
    finally:
        res = val_1 / val_2
    return res

print(may_func())