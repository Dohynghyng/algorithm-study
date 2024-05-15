N = int(input())
A = [0] + list(map(int,input().split()))
dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(0,i):
        if dp[i] <= dp[j] and A[i] > A[j]:
            dp[i] = dp[j] + 1

print(max(dp))
