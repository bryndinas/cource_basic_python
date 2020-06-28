from itertools import count
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [itm for itm in my_list if my_list.count(itm) == 1]
print(new_list)


