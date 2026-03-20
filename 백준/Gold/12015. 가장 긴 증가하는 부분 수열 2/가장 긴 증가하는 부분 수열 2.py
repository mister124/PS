import sys
from bisect import bisect_left

input = sys.stdin.readline
A = int(input())
arr = list(map(int, input().split()))
stack = []
for val in arr:
    idx = bisect_left(stack, val)
    if idx == len(stack):
        stack.append(val)
    else:
        stack[idx] = val
print(len(stack))
