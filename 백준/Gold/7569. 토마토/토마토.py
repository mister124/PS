import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dq = deque()
# 6방향: 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 (h, r, c)
op = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]

for h in range(H):
    for r in range(N):
        for c in range(M):
            if board[h][r][c] == 1:
                dq.append((h, r, c))

while dq:
    h, r, c = dq.popleft()
    for dh, dr, dc in op:
        nxt_h, nxt_r, nxt_c = h + dh, r + dr, c + dc
        
        if 0 <= nxt_h < H and 0 <= nxt_r < N and 0 <= nxt_c < M:
            if board[nxt_h][nxt_r][nxt_c] == 0:
                # 이전 위치의 일수 + 1로 갱신
                board[nxt_h][nxt_r][nxt_c] = board[h][r][c] + 1
                dq.append((nxt_h, nxt_r, nxt_c))

answer = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            # 안 익은 토마토가 하나라도 있으면 -1 출력 후 즉시 종료
            if board[h][r][c] == 0:
                print(-1)
                sys.exit(0)
            answer = max(answer, board[h][r][c])

# 시작값이 1이었으므로 1을 빼서 출력
print(answer - 1)