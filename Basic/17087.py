def gcd(x,y):
    if x<y:
        x,y = y,x
    if x%y==0:
        return y
    else:
        r = x%y
        return gcd(y,r)

N,S = map(int,input().split())
L = list(map(int,input().split()))

gcd_ = abs(L[0] - S)

for l in L:
    l = abs(l-S)
    gcd_ = gcd(gcd_,l)
print(gcd_)