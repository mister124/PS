import sys

input = sys.stdin.readline
N, M = map(int, input().split())
test_case = [line.rstrip() for line in sys.stdin.readlines()]
table_w = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]
test_tables = []
for n in range(N - 7):
    for m in range(M - 7):
        test_tables.append([line[m : m + 8] for line in test_case[n : n + 8]])
answer = float("inf")
for tests in test_tables:
    count = 0
    for a, b in zip(tests, table_w):
        for i in range(8):
            if a[i] != b[i]:
                count += 1
    if min(count, 64 - count) < answer:
        answer = min(count, 64 - count)
print(answer)