import sys

N = int(input())
S = input()

Stack = []
Num_list = []

for _ in range(N):
    Num_list.append(int(sys.stdin.readline().rstrip()))


Num_stack = []

Res = 0

for s in S:
    if s=='*':
        Num_stack.append(Num_stack.pop(-2) * Num_stack.pop(-1))
    elif s=='+':
        Num_stack.append(Num_stack.pop(-2) + Num_stack.pop(-1))
    elif s=='-':
        Num_stack.append(Num_stack.pop(-2) - Num_stack.pop(-1))
    elif s=='/':
        Num_stack.append(Num_stack.pop(-2) / Num_stack.pop(-1))
    else:
        Num_stack.append(Num_list[ord(s)-ord('A')])

print('{:.2f}'.format(Num_stack.pop()))
