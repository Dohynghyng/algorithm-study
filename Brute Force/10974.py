def rec_function(N,arr,depth=0):
    if depth == N:
        print(*arr)

    else:
        for i in range(1,N+1):
            if i not in arr[:depth]:
                arr[depth] = i
                rec_function(N,arr,depth+1)

N = int(input())
arr = [0] * N
rec_function(N,arr)