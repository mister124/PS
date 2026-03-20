import sys

input = sys.stdin.readline
A = int(input())
arr = list(map(int, input().split()))
stack = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] > stack[-1]:
        stack.append(arr[i])
        continue
    if arr[i] < stack[-1]:
        idx = -1
        left, right = 0, len(stack) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[i] <= stack[mid]:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        stack[idx] = arr[i]
print(len(stack))