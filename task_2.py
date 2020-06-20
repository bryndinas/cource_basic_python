sec = int(input('Введите время в секундах \n'))
ower = int (sec //3600)
min = int ((sec % 3600) // 60)
sec = int ((sec % 3600) % 60)
print("{:02}:{:02}:{:02}".format(ower,min,sec,))

