import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
dq = deque()
for _ in range(N):
    order = input().split()
    if order[0] == "1":
        dq.appendleft(order[1])
    elif order[0] == "2":
        dq.append(order[1])
    elif order[0] == "3":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif order[0] == "4":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif order[0] == "5":
        print(len(dq))
    elif order[0] == "6":
        if not dq:
            print(1)
        else:
            print(0)
    elif order[0] == "7":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif order[0] == "8":
        if dq:
            print(dq[-1])
        else:
            print(-1)
