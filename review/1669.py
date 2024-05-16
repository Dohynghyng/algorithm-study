N = int(input())

table = [i**2 for i in range(2,int(N**0.5)+1)]
dp = [i for i in range(N+1)]

for r in table:
    for i in range(r,len(dp)):
        if i-r >= 0:
            dp[i] = min(dp[i-r]+1,dp[i])

print(dp[N])