import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = set(input().split())
B = set(input().split())
print(len(A ^ B))