N = int(input())

tree = [[0]]
dp = [[0]]

for n in range(1,N+1):
    tree.append([0] + list(map(int, input().split())) + [0])
    dp.append([0] * len(tree[n]))

dp[1][1] = tree[1][1]
for n in range(2, N + 1):
    for i in range(1, len(tree[n]) - 1):
        dp[n][i] = max(dp[n-1][i - 1], dp[n-1][i]) + tree[n][i]

print(max(dp[N]))