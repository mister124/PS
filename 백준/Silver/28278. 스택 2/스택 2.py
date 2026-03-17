import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
order = [ord.strip() for ord in sys.stdin.readlines()]
stack = []
for ord in order:
    if ord[0] == "1":
        stack.append(int(ord[2:]))
    elif ord[0] == "2":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ord[0] == "3":
        print(len(stack))
    elif ord[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ord[0] == "5":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
