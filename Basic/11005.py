N,B = map(int,input().split(' '))

S = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''
while True:
    res += S[N%B]
    N = N//B
    if N == 0:
        break

print(res[::-1])