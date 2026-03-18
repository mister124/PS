from collections import deque

N, K = map(int, input().split())
circle = deque(range(1, N + 1))
ans = []
while circle:
    for _ in range(K - 1):
        circle.rotate(-1)
    ans.append(circle.popleft())
print("<" + ", ".join(list(map(str, ans))) + ">")
