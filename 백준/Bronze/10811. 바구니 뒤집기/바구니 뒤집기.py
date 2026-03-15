import sys

input = sys.stdin.readline
N, M = map(int, input().split())
test_case = []
for _ in range(M):
    i, j = map(int, input().split())
    test_case.append([i, j])
answer = [x + 1 for x in range(N)]
for i, j in test_case:
    answer = answer[: i - 1] + list(reversed(answer[i - 1 : j])) + answer[j:]
print(" ".join(map(str, answer)))
