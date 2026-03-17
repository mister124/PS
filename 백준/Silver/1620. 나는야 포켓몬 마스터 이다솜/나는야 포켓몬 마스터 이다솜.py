import sys

input = sys.stdin.readline
N, M = map(int, input().split())
case = dict()
for i in range(N):
    case[i + 1] = input().rstrip()
reverse_case = {value: key for key, value in case.items()}
for _ in range(M):
    temp = input().strip()
    if temp.isdigit():
        print(case[int(temp)])
    else:
        print(reverse_case[temp])
