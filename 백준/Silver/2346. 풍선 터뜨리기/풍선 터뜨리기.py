import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
circle = deque([(idx + 1, val) for idx, val in enumerate(map(int, input().split()))])
while circle:
    num = circle[0][1]
    print(circle[0][0], end=" ")
    circle.popleft()
    if num > 0:
        for _ in range(num - 1):
            circle.rotate(-1)
    else:
        for _ in range(-num):
            circle.rotate(1)
