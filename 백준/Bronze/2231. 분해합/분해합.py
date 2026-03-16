import sys

input = sys.stdin.readline
N = int(input())
ans = 0
for i in range(1, N):
    if sum((map(int, str(i)))) + i == N:
        ans = i
        break
print(ans)
