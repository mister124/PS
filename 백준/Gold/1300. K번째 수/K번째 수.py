import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

left, right = 1, K
ans = 0
while left <= right:
    mid = (left + right) // 2
    count = sum(min(mid // i, N) for i in range(1, N + 1))
    if count >= K:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
