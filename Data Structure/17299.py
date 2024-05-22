N = int(input())
L = list(map(int, input().split()))

Stack = []
R = [-1] * len(L)
D = {}
for idx in range(len(L)):
    if L[idx] not in D:
        D[L[idx]] = 1
    else:
        D[L[idx]] += 1

for idx in range(len(L)):
    while Stack and D[L[Stack[-1]]] < D[L[idx]]:
        R[Stack.pop(-1)] = L[idx]
    Stack.append(idx)
print(*R)
