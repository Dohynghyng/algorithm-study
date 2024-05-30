def N_to_10(N,L):
    S = 1
    res = 0
    for l in L[::-1]:
        res += l*S
        S*=N
    return res

def T_to_N(V,B):
    res = []
    while True:
        V,n = V//B,V%B
        res.append(n)
        if V < B:
            res.append(V)
            break
    return res[::-1]

A,B = map(int,input().split())
input()
L = list(map(int,input().split()))

ten = N_to_10(A,L)
to_b = T_to_N(ten,B)
print(*to_b)
