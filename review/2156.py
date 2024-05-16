n = int(input())

table = [0]
for _ in range(n):
    table.append(int(input()))

dp = [0] * (n+1)

if n>=1:
    dp[1] = table[1]

if n>=2:
    dp[2] = table[2]  + dp[1]

if n>=3:
    for i in range(3,n+1):
        dp[i] = max(dp[i-1], dp[i-2] + table[i], dp[i-3] + table[i-1]+table[i])

print(dp[n])