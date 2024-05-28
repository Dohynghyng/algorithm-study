def fac(N):
    res = 1
    for i in range(2,N+1):
        res *= i
    return res

a = int(input())
if a==0:
    print(1)
else:
    print(fac(a))