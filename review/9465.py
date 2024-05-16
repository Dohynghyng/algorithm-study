for _ in range(int(input())):
    n = int(input())
    table = []
    for __ in range(2):
        table.append([0] + list(map(int,input().split())))
    dp = [[0]*(n+1) for ___ in range(3)]
    for i in range(1,n+1):
        dp[2][i] = max(dp[1][i-1],dp[0][i-1])
        dp[0][i] = max(dp[1][i-1],dp[2][i-1])+table[0][i]
        dp[1][i] = max(dp[0][i-1]+table[1][i],dp[2][i-1]+table[1][i])
    print(max(dp[0][n],dp[1][n],dp[2][n]))