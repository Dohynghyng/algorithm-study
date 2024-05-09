N = int(input())

A = [0] + list(map(int,input().split()))

if max(A[1:]) < 0:
    print(max(A[1:]))

else:
    dp = [[0] * (N+1) for i in range(2)]

    for i in range(1,N+1):
        if A[i] > 0:
            dp[0][i] = dp[0][i-1] + A[i]
            dp[1][i] = dp[1][i-1] + A[i]

        else:
            dp[0][i] = max(dp[0][i-1]+A[i],dp[1][i-1])
            dp[1][i] = dp[1][i-1] + A[i]

        if dp[0][i] < 0:
            dp[0][i] = 0
        if dp[1][i] < 0:
            dp[1][i] = 0

    print(max(dp[0][1:]))