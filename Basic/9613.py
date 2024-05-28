import sys

def gcd(x, y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        r = x % y
        res = gcd(y, r)
        return res

for _ in range(int(sys.stdin.readline())):
    L = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
    res = 0

    for x in range(0, len(L)):
        for y in range(x+1, len(L)):
            res += gcd(L[x], L[y])
    print(res)