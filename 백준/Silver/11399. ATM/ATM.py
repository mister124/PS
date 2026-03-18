import sys

input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
P.sort()
ans = [(len(P) - x) * val for x, val in enumerate(P)]
print(sum(ans))
