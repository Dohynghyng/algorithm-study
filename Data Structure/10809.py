S = input()

a = ord('a')
z = ord('z')
a_z = [asc for asc in range(a,z+1)]
res = []
for asci in a_z:
    s = chr(asci)
    try:
        res.append(S.index(s))
    except:
        res.append(-1)
print(*res)