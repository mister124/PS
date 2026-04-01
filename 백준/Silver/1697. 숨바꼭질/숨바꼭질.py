from collections import deque

N, K = map(int, input().split())
dq = deque()

visited = [-1] * 100001
visited[N] = 0
dq.append(N)
while dq:
    x = dq.popleft()
    if x == K:
        print(visited[x])
        break
    for nxt in [x - 1, x + 1, x * 2]:
        if 0 <= nxt <= 100000 and visited[nxt] == -1:
            visited[nxt] = visited[x] + 1
            dq.append(nxt)
