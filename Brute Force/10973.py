def check_next(arr, N):
    index = -1
    for n in range(N-1,0,-1):
        if arr[n-1] > arr[n]:
            index = n-1
            break
    if index==-1:
        return [-1]

    for i in range(N-1,index,-1):
        if arr[index] > arr[i]:
            arr[index], arr[i] = arr[i], arr[index]
            break

    arr[index+1:] = sorted(arr[index+1:])[::-1]
    return arr

N = int(input())
A = list(map(int,input().split()))
print(*check_next(A,N))
