while True:
    x = input()
    if x.isdigit():
        x = int (x)
        break
res = 0
while x and res !=9:
    tmp = x%10
    if tmp > res:
        res = tmp
    x //=10
print(res)