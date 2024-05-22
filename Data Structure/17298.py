N = int(input())
L = list(map(int,input().split()))
R = [-1] * N
Stack = []

for i in range(N):
    if Stack:
        while Stack and L[Stack[-1]] < L[i]:
            R[Stack.pop(-1)] = L[i]
    Stack.append(i)
print(*R)