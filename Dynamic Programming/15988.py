T = int(input())
N = []

for _ in range(T):
    N.append(int(input()))

dp = [0] * (max(N)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(N) + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    dp[i] = dp[i] % 1000000009

for n in N:
    print(dp[n])