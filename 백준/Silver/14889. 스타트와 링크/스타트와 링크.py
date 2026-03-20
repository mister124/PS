from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
ans = float("inf")
team1 = []


def backtrack(start):
    global ans
    if len(team1) == N // 2:
        team2 = [i for i in range(N) if i not in team1]
        t1, t2 = 0, 0
        for p1, p2 in combinations(team1, 2):
            t1 += S[p1][p2] + S[p2][p1]
        for p1, p2 in combinations(team2, 2):
            t2 += S[p1][p2] + S[p2][p1]
        ans = min(ans, abs(t1 - t2))
        return
    for i in range(start, N):
        team1.append(i)
        backtrack(i + 1)
        team1.pop()


team1.append(0)
backtrack(1)
print(ans)
