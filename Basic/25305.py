N,k = map(int,input().split(' '))

a = list(map(int,input().split(' ')))
a.sort()
a = a[::-1]
print(a[k-1])