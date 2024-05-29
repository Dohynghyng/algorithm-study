import sys

L = [1] * 1000001
L[0],L[1] = False,False
for idx in range(2,1000001):
    for i in range(idx*2,1000001,idx):
        L[i]=0

for _ in range(int(sys.stdin.readline())):
    a = int(sys.stdin.readline())
    count=0
    for idx in range(2,a//2+1):
        if L[idx] and L[a-idx]:
            count+=1
    print(count)