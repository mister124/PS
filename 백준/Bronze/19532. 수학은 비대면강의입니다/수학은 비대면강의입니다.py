import sys

input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())
ans = 0
for x in range(-999, 1000):
    if ans != 0:
        break
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            ans = f"{x} {y}"
            break
print(ans)
