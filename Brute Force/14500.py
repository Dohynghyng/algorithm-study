n,m = list(map(int,input().split()))
table = []
for i in range(n):
    table.append(list(map(int,input().split())))

def search(arr,y_pos,x_pos):
    res = 0
    for a in arr:
        value = 0
        for y,x in a:
            y_,x_ = y+y_pos,x+x_pos
            if 0 <= y_ < n and 0<= x_ < m:
                value += table[y_][x_]
            else:
                value = 0
                break
        res = max(res,value)
    return res


# y x
arr = [[[0,0],[0,1],[0,2],[0,3]],
       [[0,0],[1,0],[2,0],[3,0]],
       [[0,0],[1,0],[2,0],[2,1]],
       [[0,0],[1,0],[0,1],[0,2]],
       [[0,0],[0,1],[1,1],[2,1]],
       [[0,2],[1,2],[1,1],[1,0]],
       [[0,0],[1,0],[2,0],[2,-1]],
       [[0,0],[1,0],[1,1],[1,2]],
       [[0,0],[1,0],[2,0],[0,1]],
       [[0,0],[0,1],[0,2],[1,2]],
       [[0,0],[1,0],[1,1],[2,1]],
       [[0,0],[0,1],[1,0],[1,-1]],
       [[0,0],[1,0],[1,-1],[2,-1]],
       [[0,0],[0,1],[1,1],[1,2]],
       [[0,0],[0,1],[0,2],[1,1]],
       [[0,0],[1,0],[2,0],[1,-1]],
       [[0,0],[1,0],[1,1],[1,-1]],
       [[0,0],[1,0],[2,0],[1,1]],
       [[0,0],[0,1],[1,0],[1,1]]]

res = 0

for y in range(n):
    for x in range(m):
        res = max(search(arr,y,x),res)

print(res)