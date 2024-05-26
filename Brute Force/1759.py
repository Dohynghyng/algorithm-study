import itertools

L, C = map(int, input().split())

arr = sorted(input().split())
iters = itertools.combinations(arr,L)

for iter in iters:
    res = ''
    cond1 = False
    cond2 = 0
    for i in iter:
        if i in 'aeiou':
            cond1 = True
        else:
            cond2 += 1
        res += i
    if cond1 and cond2 >= 2:
        print(res)
