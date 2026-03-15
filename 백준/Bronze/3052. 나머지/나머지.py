import sys

num_list = list(map(int, sys.stdin.readlines()))
answer = [x % 42 for x in num_list]
print(len(set(answer)))
