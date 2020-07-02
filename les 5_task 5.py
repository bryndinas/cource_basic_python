with open('task_5.txt', 'w', encoding='UTF -8') as my_file:
    my_file.write('5 6 7 8')
with open('task_5.txt', 'r', encoding='UTF -8') as my_file:
    sum = 0
    for i in my_file:
        my_list = i.split()
        print(my_list)
    for i in range(len(my_list)):
        old_value = my_list[i]
        new_value = int (old_value)
        my_list[i] = new_value
        sum += new_value
print(f'Сумма всех чисел:  {sum}')



