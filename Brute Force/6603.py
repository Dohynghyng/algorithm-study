import itertools

cnt = 0

while True:
    try:
        table = list(map(int,input().split()))
    except:
        break
    table = table[1:]
    table.sort()
    iters = itertools.combinations(table,6)
    for iter in iters:
        print(*iter)
    print()