import sys

input = sys.stdin.readline
num_list = list(map(int, sys.stdin.readlines()))
num_max = max(num_list)
print(num_max)
print(num_list.index(num_max) + 1)
