import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

for r in range(9):
    for c in range(9):
        num = board[r][c]
        if num:
            rows[r].add(num)
            cols[c].add(num)
            boxes[(r // 3) * 3 + c // 3].add(num)

empty = [(r, c) for r in range(9) for c in range(9) if board[r][c] == 0]


def backtrack(idx):
    if idx == len(empty):
        for row in board:
            print(*row)
        sys.exit()
        return
    r, c = empty[idx]
    box = (r // 3) * 3 + c // 3
    for num in range(1, 10):
        if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
            board[r][c] = num
            rows[r].add(num)
            cols[c].add(num)
            boxes[box].add(num)
            backtrack(idx + 1)
            board[r][c] = 0
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[box].remove(num)


backtrack(0)
