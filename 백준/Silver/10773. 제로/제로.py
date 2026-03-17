import sys

input = sys.stdin.readline
stack = []
K = int(input())
for _ in range(K):
    ans = int(input())
    if ans == 0:
        stack.pop()
    else:
        stack.append(ans)
print(sum(stack))
