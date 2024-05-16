import sys
import math

n = int(input())

value = [[0,0,0]]
for _ in range(n):
    value.append(list(map(int,input().split())))

dp = [[0,0,0] for i in range(n+1)]

dp[1] = value[1]
res = []

for c in range(0,3):
    dp[1] = [math.inf, math.inf, math.inf]
    dp[1][c] = value[1][c]
    for i in range(2,n+1):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + value[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + value[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + value[i][2]

    dp[n][c] = math.inf
    res.append(min(dp[n]))

print(min(res))