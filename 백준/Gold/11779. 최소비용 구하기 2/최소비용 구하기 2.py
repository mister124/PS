import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
start, end = map(int, input().split())

INF = float('inf')
dist = [INF] * (n + 1)
prev_node = [0] * (n + 1)  # 이전 노드를 기록할 배열
dist[start] = 0

hq = [(0, start)]

while hq:
    w, node = heapq.heappop(hq)
    
    if dist[node] < w:
        continue
        
    for nxt_node, edge_w in graph[node]:
        cost = w + edge_w
        if cost < dist[nxt_node]:
            dist[nxt_node] = cost
            prev_node[nxt_node] = node  # 최단 경로 갱신 시 직전 노드 기록
            heapq.heappush(hq, (cost, nxt_node))

# 1. 도착점부터 시작점까지 경로 역추적
path = []
curr = end
while curr != 0:
    path.append(curr)
    curr = prev_node[curr]

# 2. 역순으로 담겼으므로 올바른 순서로 뒤집기
path.reverse()

print(dist[end])
print(len(path))
print(*path)