arr = []
arr.append(int(input()))

count = 0

while 1 not in arr:
    temp_arr = []
    count += 1
    for v in arr:
        if v%3==0:
            temp_arr.append(int(v/3))
        if v%2==0:
            temp_arr.append(int(v/2))
        temp_arr.append(v-1)
    arr = temp_arr

print(count)
