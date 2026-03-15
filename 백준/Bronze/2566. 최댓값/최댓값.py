import sys

test_case = [list(map(int, nm.split())) for nm in sys.stdin.readlines()]
find_max = [max(nm) for nm in test_case]
num_max = max(find_max)
print(num_max)
for n, line in enumerate(test_case):
    if num_max in line:
        print(n + 1, line.index(num_max) + 1)
