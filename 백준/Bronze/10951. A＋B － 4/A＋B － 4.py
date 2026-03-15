import sys

input = sys.stdin.readline
test_case = sys.stdin.readlines()
for case in test_case:
    print(sum(map(int, case.split())))
