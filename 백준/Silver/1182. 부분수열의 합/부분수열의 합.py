import sys

input = sys.stdin.readline
N, S = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0

def dfs(idx, current_sum):
    global cnt
    if idx == N:
        if current_sum == S:
            cnt += 1
        return
    dfs(idx + 1, current_sum)
    dfs(idx + 1, current_sum + num[idx])

dfs(0, 0)
if S == 0:
    cnt -= 1

print(cnt)