import sys

input = sys.stdin.readline
n, m = map(int, input().split())
art = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer1 = 0
answer2 = 0

for i in range(n):
    for j in range(m):
        if art[i][j] == 1:
            answer1 += 1
            area = 1
            art[i][j] = 0
            art_stack = [(i, j)]
            while art_stack:
                x, y = art_stack.pop()
                for dir in range(4):
                    nxt_i, nxt_j = x + dx[dir], y + dy[dir]
                    if 0 <= nxt_i < n and 0 <= nxt_j < m:
                        if art[nxt_i][nxt_j] == 1:
                            art_stack.append((nxt_i, nxt_j))
                            art[nxt_i][nxt_j] = 0
                            area += 1
            answer2 = max(answer2, area)

print(answer1)
print(answer2)
