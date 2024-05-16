A = []

for _ in range(9):
    A.append(int(input()))

res = -1
for i in range(0,8):
    for j in range(i+1,9):
        res = sum(A[0:i] + A[i+1:j] + A[j+1:])
        if res == 100:
            A.pop(j)
            A.pop(i)
            break
    if res == 100:
        break

A.sort()
for a in A:
    print(a)
