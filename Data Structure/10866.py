from collections import deque
import sys

Q = deque()

for _ in range(int(sys.stdin.readline())):
    I = list(sys.stdin.readline().rstrip().split())
    if I[0] == 'push_front':
        Q.appendleft(int(I[1]))
    elif I[0] == 'push_back':
        Q.append(int(I[1]))
    elif I[0] == 'pop_front':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif I[0] == 'pop_back':
        if Q:
            print(Q.pop())
        else:
            print(-1)
    elif I[0] == 'size':
        print(len(Q))
    elif I[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif I[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif I[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)