import sys

input = sys.stdin.readline
K, N = map(int, input().split())
arr_k = [int(input()) for _ in range(K)]
ans = 0
left, right = 1, max(arr_k)
while left <= right:
    mid = (left + right) // 2
    total = sum(k // mid for k in arr_k)
    if total >= N:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
