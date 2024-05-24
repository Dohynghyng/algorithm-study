N = int(input())
l = list(map(int, input().split(' ')))
counter = 0
for l_ in l:
    c = 0
    for i in range(1, l_ + 1):
        if l_ % i == 0:
            c += 1
    if c == 2:
        counter += 1
print(counter)