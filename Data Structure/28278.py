import sys

L = []

for _ in range(int(sys.stdin.readline())):
    I_L = list(map(int,sys.stdin.readline().split()))
    if I_L[0] == 1:
        L.append(I_L[1])
    elif I_L[0] == 2:
        if len(L)==0:
               print(-1)
        else:
            print(L.pop())
    elif I_L[0] == 3:
        print(len(L))
    elif I_L[0] == 4:
        if len(L)==0:
            print(1)
        else:
            print(0)
    elif I_L[0] == 5:
        if len(L)==0:
               print(-1)
        else:
            print(L[-1])