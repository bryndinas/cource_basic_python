product_teamplate = {
    'название':("имя товара", str),
    'цена':("стоимость товара", int),
    'количество':("количество товара", int),
    'ед.':("единицы измерения (шт, кг,)", int),
}

next_enter = True
auto_inc = 1
product_list =[]
while next_enter:
    product = {}
    for key, value in product_teamplate.items():
        while True:
            user_value = input(f'{value[0]} \n')
            try:
                user_value = value[1](user_value)
            except ValueError:
                print(f"Не верно")
                continue
            product[key] = user_value
            break
    product_list.append((auto_inc,product))
    auto_inc+=1

    while True:
        next_add = input("Добавить еще продукт? Да/Нет \n")
        if next_add.lower() in ('да', 'нет'):
            next_enter = next_add.lower() == 'да'
            break
        else:
            print('Неверный ввод, повторите попытку')
print(product_list)
product_analytics = {}
for key in product_teamplate:
    result =[]
    for itn in product_list:
        result.append((itn[1][key]))
    product_analytics[key]=result
print(product_analytics)