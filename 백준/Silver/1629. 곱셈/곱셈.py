import sys

# 재귀 한도 해제 (분할 정복 시 깊이 방지)
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def power(a, b, c):
    if b == 1:
        return a % c
    temp = power(a, b // 2, c)

    if b % 2 == 0:
        return (temp * temp) % c
    else:
        return (temp * temp * a) % c

A, B, C = map(int, input().split())
print(power(A, B, C))