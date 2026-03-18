import sys

input = sys.stdin.readline
N, K = map(int, input().split())
val = []
for _ in range(N):
    val.append(int(input()))

len = 0
for v in val[::-1]:
    len += K // v
    K = K % v
    if K == 0:
        break
print(len)
