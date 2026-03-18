import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
qs_op = list(map(int, input().split()))
qs_val = list(map(int, input().split()))
QS = [val for idx, val in enumerate(qs_val) if qs_op[idx] == 0]
QS = deque(reversed(QS))
M = int(input())
for num in map(int, input().split()):
    QS.append(num)
    print(QS.popleft(), end=" ")
