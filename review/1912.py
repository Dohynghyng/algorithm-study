n = int(input())
A = [0] + list(map(int,input().split()))
dp = [0] * (n+1)

dp[1] = A[1]

for idx in range(2,n+1):
    if dp[idx-1] >= 0:
        dp[idx] = dp[idx-1] + A[idx]
    else:
        dp[idx] = A[idx]

print(max(dp[1:]))