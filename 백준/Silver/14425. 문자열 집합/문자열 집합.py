import sys

N, M = map(int, sys.stdin.readline().split())
N_set = set()
for i in range(N):
    N_set.add(sys.stdin.readline().strip())

ans = 0
for i in range(M):
    if sys.stdin.readline().strip() in N_set:
        ans += 1

print(ans)
