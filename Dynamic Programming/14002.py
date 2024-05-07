N = int(input())
A = [0] + list(map(int,input().split()))

dp = [0] * (N+1)
dp[1] = 1

for i in range(2,N+1):
    value = 0
    for j in range(1,i):
        if A[i] > A[j]:
            if value < dp[j]:
                value = dp[j]

    dp[i] = value + 1

print(max(dp))

order = max(dp)
res = []
for i in range(N,0,-1):
    if dp[i] == order:
        res.append(A[i])
        order -= 1

res.reverse()
print(*res)
