n = int(input())
A = [0] + list(map(int,input().split()))
dp = [0] * (n+1)

res = 0

for i in range(1,n+1):
    if dp[i-1]+A[i] > 0:
        dp[i] = dp[i-1]+A[i]
    else:
        dp[i] = 0

if max(A[1:])<0:
    print(max(A[1:]))
else:
    print(max(dp))