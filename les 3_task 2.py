def may_func ():
    try:
        name = input('Введите имя \n')
        surname = input('Введитя фамилию \n')
        city = input('Введитя город \n')
        year = int(input('Введитя год рождения \n'))
        email = int(input('Введитя email \n'))
        phon = int(input('Введитя телефон \n'))
        res = ("{},{},{},{},{},{}".format(name,surname,city,year,email,phon))
        print(res)
    except ValueError:
            print('Введите цифры')


a = print(may_func())





