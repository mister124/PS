def BackTracking():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, N + 1):
        if len(answer) == 0 or answer[-1] <= i:
            answer.append(i)
            BackTracking()
            answer.pop()


N, M = map(int, input().split())
answer = []
BackTracking()
