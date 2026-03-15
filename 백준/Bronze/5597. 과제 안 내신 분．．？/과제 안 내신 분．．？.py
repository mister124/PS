import sys

input = sys.stdin.readline
submitted = set(map(int, sys.stdin.readlines()))
students = set(range(1, 31))
students = students - submitted
print(min(students))
print(max(students))
