N, M = map(int, input().split())

def rec_loops(N, M, arr, depth=1):
    if depth == M+1:
        print(*arr)
    else:
        for idx in range(1, N+1):
            if idx not in arr[:depth-1]:
                if depth-1 ==0 or idx>arr[depth-2]:
                    arr[depth-1] = idx
                    rec_loops(N, M, arr, depth+1)

arr = [0] * M
rec_loops(N, M, arr)