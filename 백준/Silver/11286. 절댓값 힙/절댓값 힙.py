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
            output(str(heapq.heappop(heap)[1]) + "\n")
        else:
            output("0\n")
    else:
        if op < 0:
            heapq.heappush(heap, (abs(op), op))
        elif op > 0:
            heapq.heappush(heap, (abs(op), op))