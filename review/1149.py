N = int(input())

value = [[0,0,0]]
for _ in range(N):
    value.append(list(map(int,input().split())))

dp = [[0,0,0] for i in range(N+1)]

# RGB 순서
dp[1] = value[1]

for i in range(2,N+1):
     for c in range(3):
         if c == 0:
             dp[i][c] = min(dp[i-1][1], dp[i-1][2]) + value[i][c]
         if c == 1:
             dp[i][c] = min(dp[i-1][0], dp[i-1][2]) + value[i][c]
         if c == 2:
             dp[i][c] = min(dp[i-1][0], dp[i-1][1]) + value[i][c]

print(min(dp[N]))
