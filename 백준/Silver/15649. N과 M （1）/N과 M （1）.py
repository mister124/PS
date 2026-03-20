from itertools import permutations

N, M = map(int, input().split())
arr = list(permutations(range(1, N + 1), M))
for p in arr:
    print(" ".join(map(str, p)))