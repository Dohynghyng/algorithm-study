N = int(input())

idx = 1
res = []
while N!=1:
    if idx==N:
        break
    idx+=1
    if N%idx == 0:
        res.append(idx)
        N = N//idx
        idx = 1

for r in res:
    print(r)