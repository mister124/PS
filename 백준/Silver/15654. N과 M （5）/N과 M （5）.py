import sys

input = sys.stdin.readline
N, M = map(int, input().split())

num = sorted(list(map(int, input().split())))
visited = [False] * N
stack = []

def backtracking(depth):
    if depth == M:
        print(*stack)
        return 
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            stack.append(num[i])            
            backtracking(depth + 1)
            stack.pop()
            visited[i] = False

backtracking(0)