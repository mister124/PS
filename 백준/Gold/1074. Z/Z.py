import sys

N, r, c = map(int, sys.stdin.readline().split())

def z_order(n, row, col):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    area = half * half  
    if row < half and col < half:
        return z_order(n - 1, row, col)
    elif row < half and col >= half:
        return area + z_order(n - 1, row, col - half)
    elif row >= half and col < half:
        return 2 * area + z_order(n - 1, row - half, col)
    else:
        return 3 * area + z_order(n - 1, row - half, col - half)

print(z_order(N, r, c))