N,K = map(int,input().split())

dp = [[0] * (N+1) for _ in range(K+1)]
dp[1][1] = 1
if K==1:
    print(1)
else:
    dp[2] = [1] * (N+1)

    for i in range(3,K+1):
        for j in range(N+1):
            dp[i][j] = sum(dp[i-1][j:])

    print(sum(dp[K])%1000000000)