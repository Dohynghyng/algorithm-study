n = int(input())

A = [0] + list(map(int,input().split()))
dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(i-1,-1,-1):
        if A[j] < A[i]:
            dp[i] = max(dp[i],dp[j] + A[i])

print(dp)
print(max(dp))