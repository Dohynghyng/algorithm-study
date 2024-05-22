S = input()

Stack = ''
Que = ''
Result = ''

state = 0
for s in S:
    if s == '<':
        state = 1
        Result += Stack[::-1]
        Stack = ''
    elif s == ' ' and not state:
        Result += Stack[::-1]
        Stack = ''

    if state:
        Result += s
    else:
        if s == ' ':
            Result += Stack[::-1]
            Result += ' '
            Stack = ''
        else:
            Stack += s

    if s == '>':
        state = 0

Result += Stack[::-1]
print(Result)