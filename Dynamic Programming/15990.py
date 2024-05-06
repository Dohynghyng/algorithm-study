idxs = []
for _ in range(int(input())):
    idxs.append(int(input()))
max_v = max(idxs)

dp = [[0,0,0] for _ in range(max_v+1)]

dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4,max_v+1):
    dp[i][0] = dp[i-1][1]%1000000009 + dp[i-1][2]%1000000009
    dp[i][1] = dp[i-2][0]%1000000009 + dp[i-2][2]%1000000009
    dp[i][2] = dp[i-3][0]%1000000009 + dp[i-3][1]%1000000009

for idx in idxs:
    print(sum(dp[idx])%1000000009)