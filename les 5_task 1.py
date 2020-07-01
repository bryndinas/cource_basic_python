my_file = open('file_text.txt', 'w', encoding='UTF-8')
try:
    my_file.write(input('Введите текст:' '\n'))
finally:
    my_file.close()


