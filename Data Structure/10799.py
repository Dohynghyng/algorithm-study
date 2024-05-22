I = input()

I = I.replace('()','R')
Stack = []

res = 0

for i in I:
    if i=='(':
        Stack.append('(')
    elif i==')':
        Stack.pop(-1)
        res += 1
    elif i=='R':
        res += len(Stack)

print(res)