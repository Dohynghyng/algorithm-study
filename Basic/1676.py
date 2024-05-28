def fact(N):
    if N == 0:
        return 1
    res = 1
    for i in range(2, N + 1):
        res *= i
    return res

V = int(input())
res = fact(V)
res = str(res)[::-1]

count = 0
for idx in range(0, len(res)):
    if res[idx] == '0':
        count += 1
    else:
        break

print(count)