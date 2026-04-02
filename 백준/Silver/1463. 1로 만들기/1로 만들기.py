
import sys
from collections import deque

N = int(sys.stdin.readline())
visited = [-1] * (N + 1)
visited[1] = 0
dq = deque([1])
while dq:
    x = dq.popleft()

    if x == N:
        print(visited[x])
        break

    for nxt in (x + 1, x * 2, x * 3):
        if nxt <= N and visited[nxt] == -1:
            visited[nxt] = visited[x] + 1
            dq.append(nxt)
