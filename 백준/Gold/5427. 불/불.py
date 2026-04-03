import sys
from collections import deque

input = sys.stdin.readline

def solve():
    w, h = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]
    
    # 시간 저장 배열 (-1: 미방문)
    fire_time = [[-1] * w for _ in range(h)]
    player_time = [[-1] * w for _ in range(h)]
    
    fire_dq = deque()
    player_dq = deque()
    
    for r in range(h):
        for c in range(w):
            if board[r][c] == '*':
                fire_dq.append((r, c))
                fire_time[r][c] = 0
            elif board[r][c] == '@':
                player_dq.append((r, c))
                player_time[r][c] = 0
                
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 1. 불의 확산 시간 계산
    while fire_dq:
        r, c = fire_dq.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                if board[nr][nc] != '#' and fire_time[nr][nc] == -1:
                    fire_time[nr][nc] = fire_time[r][c] + 1
                    fire_dq.append((nr, nc))
                    
    # 2. 상근이의 이동
    while player_dq:
        r, c = player_dq.popleft()
        
        # 현재 위치가 가장자리라면 다음 이동 시 탈출 성공이므로 즉시 출력 후 함수 종료
        if r == 0 or r == h - 1 or c == 0 or c == w - 1:
            print(player_time[r][c] + 1)
            return
            
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < h and 0 <= nc < w:
                # 벽이 아니고, 상근이가 아직 방문하지 않은 곳
                if board[nr][nc] != '#' and player_time[nr][nc] == -1:
                    # 불이 아예 오지 않거나(-1), 불보다 상근이가 먼저 도착하는 경우
                    if fire_time[nr][nc] == -1 or fire_time[nr][nc] > player_time[r][c] + 1:
                        player_time[nr][nc] = player_time[r][c] + 1
                        player_dq.append((nr, nc))
                        
    # 큐가 빌 때까지 가장자리에 도달하지 못한 경우
    print("IMPOSSIBLE")

T = int(input())
for _ in range(T):
    solve()