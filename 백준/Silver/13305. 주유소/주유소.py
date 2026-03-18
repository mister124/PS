import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
min_price = price[0]
for i in range(N - 1):
    min_price = min(min_price, price[i])
    ans += min_price * dist[i]

print(ans)