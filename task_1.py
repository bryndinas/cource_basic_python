name = 'Artem'
age = 25
while True:
    name = input('Введите имя \n')
    if name.isalpha():
        name = str (name)
        break
print(name)
while True:
    age = input('Введите возраст \n')
    if age .isdigit():
        age= int(age)
        break
print(age)