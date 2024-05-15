import sys

num = int(input())

n = []
for _ in range(num):
    n.append(int(sys.stdin.readline()))

dp = [0] * (max(n)+3)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for idx in range(4,max(n)+1):
    dp[idx] = sum(dp[idx-3:idx])

for idx in n:
    print(dp[idx])