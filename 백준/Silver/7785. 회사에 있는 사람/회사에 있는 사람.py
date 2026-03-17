import sys

input = sys.stdin.readline
n = int(input())
people = set()
for _ in range(n):
    name, state = input().split()
    if name in people:
        people.remove(name)
    else:
        people.add(name)
people = sorted(list(people), reverse=True)
for i in people:
    print(i)
