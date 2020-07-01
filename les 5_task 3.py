with open('task_3.txt', 'r', encoding='UTF-8') as me_file:
    for i in me_file:
        a = i.split()
        b = (a[1])
        c = int(b)
        if c < 20000:
            print(a[0])





