import sys

Stack = []

for _ in range(int(sys.stdin.readline())):
    a = list(sys.stdin.readline().rstrip().split())
    if a[0] == 'push':
        Stack.append(int(a[1]))
    elif a[0] == 'pop':
        if len(Stack) != 0:
            print(Stack.pop(-1))
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(Stack))
    elif a[0] == 'empty':
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if len(Stack) != 0:
            print(Stack[-1])
        else:
            print(-1)
