import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    stack = []
    ans = input().strip()
    for chr in ans:
        if chr == "(":
            stack.append(chr)
        else:
            if len(stack) == 0:
                stack.append(chr)
            elif chr == stack[-1]:
                stack.append(chr)
            else:
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")