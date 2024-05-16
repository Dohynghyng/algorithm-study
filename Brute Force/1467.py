target = list(map(int,input().split()))

date = [0,0,0]
max_val = [16,29,20]
counter = 0

while True:
    counter += 1
    for i in range(3):
        date[i] += 1
        if date[i] == max_val[i]:
            date[i]=1

    if date==target:
        print(counter)
        break