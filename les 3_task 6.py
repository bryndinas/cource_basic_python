def my_func (word: str):
    return word.title()
word_str = input('Введите текст : ')
new_list = word_str.split()
result = ''
for i in range(0, len(new_list)):
    total = my_func(new_list[i])
    result = result + total + ' '
print(result.rstrip())