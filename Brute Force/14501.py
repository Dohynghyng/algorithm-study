def rec_func(depth=0,res=0):
    global ans
    tmp = res
    for i in range(depth, N):
        if day_table[i] + i < N+1:
            ans = max(ans,tmp+price_table[i])
            rec_func(i+day_table[i], tmp+price_table[i])

N = int(input())
day_table = []
price_table = []
ans = 0

for i in range(N):
    d,p = map(int, input().split())
    day_table.append(d)
    price_table.append(p)
rec_func()
print(ans)