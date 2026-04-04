import sys
from collections import deque

input = sys.stdin.readline


def bfs(L, K, D):
    visited = [[-1 for _ in range(L)] for _ in range(L)]
    dq = deque([K])
    visited[K[0]][K[1]] = 0
    op = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    while dq:
        r, c = dq.popleft()
        if r == D[0] and c == D[1]:
            return visited[r][c]
        for dr, dc in op:
            nr, nc = r + dr, c + dc
            if 0 <= nr < L and 0 <= nc < L:
                if visited[nr][nc] == -1:
                    dq.append([nr, nc])
                    visited[nr][nc] = visited[r][c] + 1


T = int(input())
for _ in range(T):
    l = int(input())
    k = list(map(int, input().split()))
    d = list(map(int, input().split()))
    print(bfs(l, k, d))
