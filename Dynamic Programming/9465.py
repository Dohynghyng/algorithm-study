T = int(input())

for t in range(T):
    N = int(input())

    dp = [[0,0,0] for _ in range(N+1)]

    score = []

    score.append([0] + list(map(int,input().split())))
    score.append([0] + list(map(int,input().split())))
    idx = 0
    for n in range(1,N+1):
        if dp[n-1][2] + score[0][n] > dp[n-1][1] + score[0][n]:
            dp[n][0] = dp[n - 1][2] + score[0][n]
        else:
            dp[n][0] = dp[n-1][1] + score[0][n]
        if dp[n-1][2] + score[1][n] > dp[n-1][0] + score[1][n]:
            dp[n][1] = dp[n-1][2] + score[1][n]
        else:
            dp[n][1] = dp[n-1][0] + score[1][n]
        dp[n][2] = max(dp[n-1][:2])
    print(max(dp[N]))
