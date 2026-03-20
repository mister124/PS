N = int(input())
ans = 0
col = [False] * N
left = [False] * (2 * N)
right = [False] * (2 * N)


def backtrack(row):
    global ans
    if row == N:
        ans += 1
        return
    for i in range(N):
        if not col[i] and not left[row + i] and not right[row - i + N]:
            col[i] = left[row + i] = right[row - i + N] = True
            backtrack(row + 1)
            col[i] = left[row + i] = right[row - i + N] = False


backtrack(0)
print(ans)
