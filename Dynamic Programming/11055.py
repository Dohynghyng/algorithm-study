N = int(input())

table = [0]+ list(map(int,input().split()))
dp = [0 for _ in range(len(table))]

for i in range(1,N+1):
    for j in range(0,i):
        if table[i] > table[j]:
            dp[i] = max(dp[i],dp[j]+table[i])

print(max(dp))