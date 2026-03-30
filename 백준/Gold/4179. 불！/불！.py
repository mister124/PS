import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]
fire_time = [[-1] * C for _ in range(R)]
j_time = [[-1] * C for _ in range(R)]
fire_q = deque()
j_q = deque()
for r in range(R):
    for c in range(C):
        if maze[r][c] == 'F':
            fire_q.append((r, c))
            fire_time[r][c] = 0
        elif maze[r][c] == 'J':
            j_q.append((r, c))
            j_time[r][c] = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while fire_q:
    r, c = fire_q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if maze[nr][nc] != '#' and fire_time[nr][nc] == -1:
                fire_time[nr][nc] = fire_time[r][c] + 1
                fire_q.append((nr, nc))
while j_q:
    r, c = j_q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            print(j_time[r][c] + 1)
            sys.exit(0)
        if maze[nr][nc] != '#' and j_time[nr][nc] == -1:
            if fire_time[nr][nc] == -1 or fire_time[nr][nc] > j_time[r][c] + 1:
                j_time[nr][nc] = j_time[r][c] + 1
                j_q.append((nr, nc))
print("IMPOSSIBLE")