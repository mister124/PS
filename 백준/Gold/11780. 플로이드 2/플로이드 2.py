import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = float("inf")

dist = [[INF] * (n + 1) for _ in range(n + 1)]
nxt_node = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
        nxt_node[a][b] = b  # a에서 b로 가기 위한 다음 방문 노드는 b

# 플로이드-워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                # i에서 j로 갈 때, i에서 k로 가는 경로의 첫 번째 노드를 따라감
                nxt_node[i][j] = nxt_node[i][k]

# 비용 배열 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

# 경로 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 갈 수 없거나 자기 자신인 경우
        if dist[i][j] == INF or i == j:
            print(0)
        else:
            path = [i]
            curr = i
            # 목적지 j에 도달할 때까지 다음 노드 추적
            while curr != j:
                curr = nxt_node[curr][j]
                path.append(curr)

            print(len(path), *path)
