from itertools import permutations

N, M = map(int, input().split())
arr = list(permutations(range(1, N + 1), M))
arr_new = [list(p) for p in arr if list(p) == sorted(list(p))]
for p in arr_new:
    print(" ".join(map(str, p)))
