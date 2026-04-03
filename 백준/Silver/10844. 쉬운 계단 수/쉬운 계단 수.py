import sys

N = int(sys.stdin.readline())
MOD = 1_000_000_000

dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1] % MOD
        elif j == 9:
            dp[i][j] = dp[i-1][8] % MOD
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD

print(sum(dp[N]) % MOD)