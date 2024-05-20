length_list = []
for i in range(1,10):
    length_list.append(9*(10**(i-1))*i)

# N이 2717 이라면
N = int(input())
length = len(str(N))

# 1~9, 10~99, 100~999 > 최대 자리수 밑의 수를 계산
res = sum(length_list[:length-1])

# 1000~2717까지 계산
res += (N - (10**(length-1)) + 1) *length

print(res)