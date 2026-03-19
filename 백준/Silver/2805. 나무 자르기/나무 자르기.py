import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)
height = 0
while left <= right:
    mid = (left + right) // 2
    get = sum([tree - mid for tree in trees if tree > mid])
    if get < M:
        right = mid - 1
    else:
        height = mid
        left = mid + 1
print(height)
