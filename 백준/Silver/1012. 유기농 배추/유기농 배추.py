import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, input().split())
        board[X][Y] = 1
    dq = deque()
    cnt = -1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r in range(M):
        for c in range(N):
            if board[r][c] == 1:
                dq.append((r, c))
                board[r][c] = cnt
                while dq:
                    rp, cp = dq.popleft()
                    for dir in range(4):
                        nxt_r, nxt_c = rp + dr[dir], cp + dc[dir]
                        if (
                            0 <= nxt_r < M
                            and 0 <= nxt_c < N
                            and board[nxt_r][nxt_c] == 1
                        ):
                            board[nxt_r][nxt_c] = cnt
                            dq.append((nxt_r, nxt_c))
                cnt -= 1
    print(-cnt - 1)
