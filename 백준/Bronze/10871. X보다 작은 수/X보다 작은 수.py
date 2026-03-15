import sys

input = sys.stdin.readline
N, X = map(int, input().split())
numbers = list(map(int, input().split()))
for i in numbers:
    if i < X:
        print(f"{i}", end=" ")
