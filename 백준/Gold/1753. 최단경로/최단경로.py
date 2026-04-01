import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = float('inf')
dist = [INF] * (V + 1)
dist[K] = 0

hq = [(0, K)]

while hq:
    w, node = heapq.heappop(hq)
    
    if dist[node] < w:
        continue
        
    for nxt_node, edge_w in graph[node]:
        cost = w + edge_w
        if cost < dist[nxt_node]:
            dist[nxt_node] = cost
            heapq.heappush(hq, (cost, nxt_node))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])