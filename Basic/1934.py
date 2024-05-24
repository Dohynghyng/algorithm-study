import sys

def gb(a, b, gy_):
    a_ = a / gy_
    return b * a_

def gy(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return gy(b, r)

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gb_ = gb(a, b, gy(a, b))
    print(int(gb_))