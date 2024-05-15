N = int(input())
Pn =[0] + list(map(int,input().split()))

dp = Pn.copy()

for i in range(1,N+1):
    val = []
    for j in range(0,i):
        val.append(dp[j]+dp[i-j])
    dp[i] = max(val)

print(dp[N])