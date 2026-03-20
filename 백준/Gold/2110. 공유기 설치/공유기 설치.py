import sys

input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = 0
left, right = 1, arr[-1] - arr[0]
while left <= right:
    mid = (left + right) // 2
    count = 1
    last = arr[0]
    for i in range(1, N):
        if arr[i] - last >= mid:
            count += 1
            last = arr[i]
    if count >= C:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
