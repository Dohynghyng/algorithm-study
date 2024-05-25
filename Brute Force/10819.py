

def func(arr, table, N,res=0, depth=0):
    if depth == N:
        temp = 0
        for idx in range(N-1):
            temp += abs(table[arr[idx]] - table[arr[idx+1]])
        res = max(temp,res)
        return res

    else:
        for i in range(0,N):
            if i not in arr[:depth]:
                arr[depth] = i
                res = func(arr,table,N,res, depth+1)
        return res

N = int(input())
table = sorted(list(map(int,input().split())))
arr = [0]*N
res = func(arr,table,N)
print(res)