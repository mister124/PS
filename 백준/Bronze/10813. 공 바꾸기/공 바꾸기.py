import sys

input = sys.stdin.readline
N, M = map(int, input().split())
test_case = []
for _ in range(M):
    i, j = map(int, input().split())
    test_case.append([i, j])
answer = [x + 1 for x in range(N)]
temp = 0
for i, j in test_case:
    temp = answer[i - 1]
    answer[i - 1] = answer[j - 1]
    answer[j - 1] = temp
print(" ".join(map(str, answer)))
