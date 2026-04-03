import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [list(input().strip()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    dq = deque([(r, c)])
    visited[r][c] = True
    color = board[r][c]
    while dq:
        curr_r, curr_c = dq.popleft()
        for i in range(4):
            nxt_r, nxt_c = curr_r + dr[i], curr_c + dc[i]
            if 0 <= nxt_r < N and 0 <= nxt_c < N:
                if not visited[nxt_r][nxt_c] and board[nxt_r][nxt_c] == color:
                    visited[nxt_r][nxt_c] = True
                    dq.append((nxt_r, nxt_c))


visited = [[False] * N for _ in range(N)]
normal_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            normal_cnt += 1
for i in range(N):
    for j in range(N):
        if board[i][j] == "G":
            board[i][j] = "R"
visited = [[False] * N for _ in range(N)]
colorblind_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            colorblind_cnt += 1
print(normal_cnt, colorblind_cnt)
