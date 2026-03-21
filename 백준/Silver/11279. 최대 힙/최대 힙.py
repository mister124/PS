import sys
import heapq

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
ops = [int(input()) for _ in range(N)]

heap = []
for op in ops:
    if op == 0:
        if heap:
            output(str(-heapq.heappop(heap)) + "\n")
        else:
            output("0\n")
    else:
        heapq.heappush(heap, -op)
