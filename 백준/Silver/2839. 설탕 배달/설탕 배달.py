N = int(input())
ans = -1
for i in range(N // 5 + 1):
    for j in range(N // 3 + 1):
        if 5 * i + 3 * j == N:
            ans = i + j
print(ans)
