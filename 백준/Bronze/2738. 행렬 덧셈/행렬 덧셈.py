import sys

input = sys.stdin.readline
N, M = map(int, input().split())
test_case = [list(map(int, nm.split())) for nm in sys.stdin.readlines()]
matrix_a = test_case[:N]
matrix_b = test_case[N:]
for a_line, b_line in zip(matrix_a, matrix_b):
    for a, b in zip(a_line, b_line):
        print(a + b, end=" ")
    print()
