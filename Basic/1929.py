import sys

def is_prime(a):
    if a==2:
        return True
    elif a==1:
        return False
    for b in range(2,int(a**0.5)+1):
        if a%b==0:
            return False
    return True

a,b = map(int,sys.stdin.readline().split())

for i in range(a,b+1):
    if is_prime(i):
        print(i)