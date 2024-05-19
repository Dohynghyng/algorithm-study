def get_longest(table,N):
    res = 1

    for y in range(N):
        count = 1
        for x in range(N-1):
            if table[y][x] == table[y][x+1]:
                count += 1
            else:
                count = 1
            res = max(res,count)

    for x in range(N):
        count = 1
        for y in range(N-1):
            if table[y][x] == table[y+1][x]:
                count += 1
            else:
                count = 1
            res = max(res,count)
    return res


N = int(input())

table = []
for i in range(N):
    table.append(list(input()))

res = 0
for y in range(N):
    for x in range(N):
        # 오른쪽 swap
        if x<N-1 and table[y][x] != table[y][x+1]:
            table[y][x],table[y][x+1] = table[y][x+1],table[y][x]
            res = max(res, get_longest(table,N))
            table[y][x],table[y][x+1] = table[y][x+1],table[y][x]
        # 아래쪽 swap
        if y<N-1 and table[y][x] != table[y+1][x]:
            table[y][x],table[y+1][x] = table[y+1][x],table[y][x]
            res = max(res, get_longest(table,N))
            table[y][x],table[y+1][x] = table[y+1][x],table[y][x]

print(res)