import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
tomato_dq = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            tomato_dq.append((r, c))
while tomato_dq:
    r, c = tomato_dq.popleft()
    for dir in range(4):
        nxt_r, nxt_c = r + dr[dir], c + dc[dir]
        if 0 <= nxt_r < N and 0 <= nxt_c < M and tomato[nxt_r][nxt_c] == 0:
            tomato[nxt_r][nxt_c] = tomato[r][c] + 1
            tomato_dq.append((nxt_r, nxt_c))
ans = 0
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 0:
            print(-1)
            sys.exit(0)
        ans = max(ans, tomato[r][c])
print(ans - 1)
