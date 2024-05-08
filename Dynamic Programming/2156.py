N = int(input())

value = [0]
for _ in range(N):
    value.append(int(input()))

dp = [0] * (N+1)

if N >= 1:
    dp[1] = value[1]
if N >= 2:
    dp[2] = dp[1] + value[2]

for i in range(3,N+1):
    dp[i] = max(dp[i-2]+value[i], dp[i-3]+value[i-1]+value[i], dp[i-1])

print(dp[N])
