N = int(input())

price = [[0,0,0] for _ in range(N+1)]
dp = [[0,0,0] for _ in range(N+1)]

for i in range(1,N+1):
    price[i] = list(map(int,input().split()))
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + price[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + price[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + price[i][2]

print(min(dp[N]))
