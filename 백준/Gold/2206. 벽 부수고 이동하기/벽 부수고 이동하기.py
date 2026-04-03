import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
MAP = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        y, x, broken = queue.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][broken]
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] == 0 and visited[ny][nx][broken] == 0:
                    visited[ny][nx][broken] = visited[y][x][broken] + 1
                    queue.append((ny, nx, broken))
                elif MAP[ny][nx] == 1 and broken == 0 and visited[ny][nx][1] == 0:
                    visited[ny][nx][1] = visited[y][x][broken] + 1
                    queue.append((ny, nx, 1))
    return -1


print(bfs())
