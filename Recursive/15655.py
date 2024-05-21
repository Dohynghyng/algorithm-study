def rec_loops(N, M, arr, table, depth=1):
    if depth == M+1:
        for a in arr:
            print(table[a-1], end=' ')
        print()
    else:
        for idx in range(1, N+1):
            if idx not in arr[:depth-1]:
                if depth-1 ==0 or idx>arr[depth-2]:
                    arr[depth-1] = idx
                    rec_loops(N, M, arr, table, depth+1)


N, M = map(int, input().split())
table = list(map(int, input().split()))
table.sort()
arr = [0] * M
rec_loops(N, M, arr, table)