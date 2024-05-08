N = int(input())

dp = [0] * (N+2)
dp[1] = 3
dp[2] = 7

for n in range(3,N+1):
    dp[n] = dp[n-2] + dp[n-1] * 2
    dp[n] = dp[n] % 9901

print(dp[N])