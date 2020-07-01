my_file = open('task_4_1.txt', 'w', encoding='UTF-8')
my_list = []
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',}

for i in open('task_4.txt',encoding='UTF-8'):
    i = i.replace(i[0:i.find(' ')], my_dict[i[0:i.find(' ')]])
    my_file.write(i)
#    x.append(i[:-1])

my_file.close()