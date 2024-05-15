N = int(input())
A = [0] + list(map(int,input().split()))
dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(0,i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))

order = max(dp)
res = []
for i in range(len(dp)-1,0,-1):
    if dp[i] == order:
        order -= 1
        res.append(A[i])
res.reverse()
print(*res)