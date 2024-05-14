N,K = map(int,input().split())
L = [idx for idx in range(1,N+1)]

num = 0
print('<',end='')
while True:
    num += K-1
    if num >= len(L):
        num = num % len(L)
    print(L.pop(num),end='')
    if L:
        print(', ',end='')
    else:
        print('>',end='')
        break
