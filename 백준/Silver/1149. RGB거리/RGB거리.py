import sys

input = sys.stdin.readline
N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]
case = case[::-1]
for i in range(1, N):
    for j in range(3):
        case[i][j] = min(
            case[i][j] + case[i - 1][(j + 1) % 3], case[i][j] + case[i - 1][(j + 2) % 3]
        )
print(min(case[-1]))
