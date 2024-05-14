import sys

S1 = list(sys.stdin.readline().rstrip())
S2 = []

for _ in range(int(sys.stdin.readline())):
    I = list(sys.stdin.readline().rstrip().split())
    if I[0] == 'L':
        if S1:
            S2.append(S1.pop())
    elif I[0] == 'D':
        if S2:
            S1.append(S2.pop())
    elif I[0] == 'B':
        if S1:
            S1.pop()
    elif I[0] == 'P':
        S1.append(I[1])


for l in S1 + S2[::-1]:
    print(l, end='')