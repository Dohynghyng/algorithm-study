B,N = input().split()
N = int(N)
B = B[::-1]
res = 0
standard = ord('A')

idx = 1
for b in B:
    try:
        b = int(b)
    except:
        b = ord(b)-standard+10
    res += b*idx
    idx *=N
print(res)