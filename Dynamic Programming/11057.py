N = int(input())

dp = [[0]*10 for _ in range(N+1)]

dp[1] = [1] * 10

for i in range(2,N+1):
    for v in range(0,10):
        dp[i][v] = sum(dp[i-1][:v+1])

print(sum(dp[N])%10007)