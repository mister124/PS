A, B = map(int, input().split())
C = int(input())
CH, CM = C // 60, C % 60
A, B = A + CH, B + CM
if B >= 60:
    A += 1
    B -= 60
print(A % 24, B)
