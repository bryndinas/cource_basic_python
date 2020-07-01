with open('task_2.txt','r', encoding='UTF-8') as my_file:
    value = 0
    for string in my_file:
     print(f"Количество слов в строке: {(len(string.split()))}")
     value += 1
print (f"Количество строк: {value}")






