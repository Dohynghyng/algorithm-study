n = int(input())
dp = [0] * (n+1)
p = [0] + list(map(int, input().split()))

dp[1] = p[1]

for i in range(2,n+1):
    max = p[i]
    for j in range(i-1,0,-1):
        temp = dp[i-j] + p[j]
        if temp < max:
            max = temp
    dp[i] = max

print(dp[n])