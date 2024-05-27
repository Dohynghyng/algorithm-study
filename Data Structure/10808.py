start_num = ord('a')
last_num = ord('z')

res = [0] * (last_num - start_num + 1)

S = input()

for s in S:
    res[ord(s)- start_num] += 1

print(*res)