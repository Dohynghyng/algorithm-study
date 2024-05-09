N = int(input())
table = [0] + list(map(int,input().split()))

dp = [1] * (N+1)
dp[0] = 0

for i in range(0,N+1):
    for j in range(0,i):
        if table[j] > table[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))