import sys

test_case = [line.rstrip() for line in sys.stdin.readlines()]
value_max = max(len(line) for line in test_case)
for i in range(value_max):
    for line in test_case:
        if i < len(line):
            print(line[i], end="")
