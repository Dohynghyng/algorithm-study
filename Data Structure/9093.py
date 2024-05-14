import sys

for _ in range(int(sys.stdin.readline())):
    text = sys.stdin.readline().rstrip().split()
    for t in text:
        print(t[::-1], end=' ')
    print()