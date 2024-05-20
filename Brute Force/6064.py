def cal(M,N,t_x,t_y):
    res = t_x
    while res <= M*N:
        if (res-t_y)%N==0:
            return res
        res += M
    return -1


for _ in range(int(input())):
    M,N,target_x,target_y = list(map(int,input().split()))
    if M<N:
        M,N = N,M
        target_x,target_y = target_y,target_x
    x,y = target_x,target_x
    count = target_x
    print(cal(M,N,target_x,target_y))