A, B, C = map(int, input().split())
if A == B and B == C:
    print(10000 + A * 1000)
if A == B and B != C:
    print(1000 + A * 100)
if B == C and C != A:
    print(1000 + B * 100)
if C == A and A != B:
    print(1000 + C * 100)
if A != B and B != C and C != A:
    print(max(A, B, C) * 100)
