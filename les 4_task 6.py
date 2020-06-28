from itertools import count

for el in count(3):
    if el > 10:
        break
    print(el)

from itertools import cycle

c=0
my_list = [1,2,3,4,8,5,6,7,8]
for el in cycle (my_list):
    if el == 3:
        print(el)
    elif el == 1:
        print(el)
    if c > 50:
        break
    c+=1
