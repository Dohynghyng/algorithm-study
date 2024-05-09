N = int(input())

A = list(map(int,input().split()))
A_r = A.copy()
A_r.reverse()

increase_dp = [1] * N
decrease_dp = [1] * N

for i in range(N):
    for j in range(0,i):
        if A[i] > A[j]:
            increase_dp[i] = max(increase_dp[j]+1,increase_dp[i])
        if A_r[i] > A_r[j]:
            decrease_dp[i] = max(decrease_dp[j] + 1, decrease_dp[i])

decrease_dp.reverse()
for i in range(N):
    decrease_dp[i] += increase_dp[i]

print(max(decrease_dp)-1)