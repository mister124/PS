import sys

input = sys.stdin.readline
N = int(input())
arr_n = list(map(int, input().split()))
M = list(map(int, input().split()))
arr_m = list(map(int, input().split()))
set_n = set(arr_n)
for num in arr_m:
    if num in set_n:
        print(1)
    else:
        print(0)