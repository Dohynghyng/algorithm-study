def two_count(n):
    count = 0
    if n<2:
        return count
    while n >= 2:
        count += n // 2
        n = n//2
    return count

def five_count(n):
    count = 0
    if n<5:
        return count
    while n >= 5:
        count += n // 5
        n = n//5
    return count

n, r = map(int, input().split())

two = two_count(n) - two_count(n - r) - two_count(r)
five = five_count(n) - five_count(n - r) - five_count(r)

print(min(two, five))
