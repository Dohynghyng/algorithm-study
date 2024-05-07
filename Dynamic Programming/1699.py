N = int(input())

dp = [i for i in range(N+1)]

root = int(N**0.5)

for r in range(2,root+1):
    for i in range(r**2,len(dp)):
        dp[i] = min(dp[i],dp[i-r**2]+1)

print(dp[N])
