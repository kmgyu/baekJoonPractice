import sys
input = sys.stdin.readline
n, k = map(int, input().split())
c = set()
for i in range(n):
    c.add(int(input()))
dp = [0] + [10001 for i in range(k)]
for coin in c:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[k] == 10001: print(-1)
else: print(dp[k])