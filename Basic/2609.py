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

a, b = map(int, input().split())

gy_ = gy(a, b)
gb_ = gb(a, b, gy_)
print(gy_)
print(int(gb_))