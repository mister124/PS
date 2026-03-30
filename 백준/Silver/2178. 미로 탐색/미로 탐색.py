import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
nm_arr = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bfs_dq = deque([(0, 0)])

while bfs_dq:
    r, c = bfs_dq.popleft()
    for dir in range(4):
        nxt_r, nxt_c = r + dx[dir], c + dy[dir]
        if 0 <= nxt_r < N and 0 <= nxt_c < M and nm_arr[nxt_r][nxt_c] == 1:
            bfs_dq.append([nxt_r, nxt_c])
            nm_arr[nxt_r][nxt_c] = nm_arr[r][c] + 1
print(nm_arr[N - 1][M - 1])
