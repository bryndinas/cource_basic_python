with open('task_2.txt','r', encoding='UTF-8') as my_file:
    value = 0
    for string in my_file:
     print(len(string.split()))
     value += 1
print (value)






