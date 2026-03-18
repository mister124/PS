from collections import deque

N = int(input())
line = deque(map(int, input().split()))
stack = []
num = 1
while stack or line:
    if line and line[0] == num:
        line.popleft()
        num += 1
        continue
    if stack and stack[-1] == num:
        stack.pop()
        num += 1
        continue
    if line and line[0] != num:
        stack.append(line.popleft())
        continue
    if stack and stack[-1] != num:
        break
if not stack and not line:
    print("Nice")
else:
    print("Sad")
