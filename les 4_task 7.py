def mу_gen (n):
    result = 1
    for i in range(1,n+1):
        result = result * i
        yield result

for i in mу_gen(10):
    print(i)