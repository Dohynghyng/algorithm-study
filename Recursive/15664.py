
def rec_loops(N, M, arr, table, depth=0):
    if depth == M:
        for a in arr:
            print(table[a], end=' ')
        print()
    else:
        prev = 0
        for idx in range(0, N):
            if depth==0 and prev!=table[idx]:
                arr[depth] = idx
                prev=table[idx]
                rec_loops(N, M, arr, table, depth+1)
            elif idx not in arr[:depth] and prev!=table[idx] and table[arr[depth-1]]<=table[idx]:
                arr[depth] = idx
                prev=table[idx]
                rec_loops(N, M, arr,table, depth+1)

N, M = map(int, input().split())
table = list(map(int, input().split()))
table.sort()

arr = [-1] * M
prev = [0] * M
rec_loops(N, M, arr, table)