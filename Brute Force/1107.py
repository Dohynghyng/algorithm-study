def check_available(channel, broken_button):
    for c in str(channel):
        if c in broken_button:
            return False
    return True

target = int(input())
N = int(input())
broken_button=[]

if N!=0:
    broken_button = input().split()

if len(broken_button) == 10:
    print(abs(100 - target))

else:
    count = 0
    while True:
        if target - count >= 0 and check_available(target - count, broken_button):
            count += len(str(target - count))
            break
        if check_available(target + count, broken_button):
            count += len(str(target + count))
            break
        count += 1

    count = min(abs(100 - target), count)

    print(count)