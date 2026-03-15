import sys

input = sys.stdin.readline
N, M = map(int, input().split())
test_case = []
for _ in range(M):
    i, j, k = map(int, input().split())
    test_case.append([i, j, k])
answer = [0] * N
for i, j, k in test_case:
    answer = answer[: i - 1] + [k for _ in range(j - i + 1)] + answer[j:]
print(" ".join(map(str, answer)))
