import sys

for _ in range(int(sys.stdin.readline())):
    Stack = []
    state = 'YES'
    text = sys.stdin.readline().rstrip()
    for t in text:
        if t == '(':
            Stack.append('(')
        elif t == ')':
            if len(Stack) == 0:
                state = 'NO'
                break
            else:
                Stack.pop(-1)
    if len(Stack) == 0 and state == 'YES':
        print('YES')
    else:
        print('NO')
