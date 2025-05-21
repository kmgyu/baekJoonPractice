n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1] + [0]*(k)
cnt = 0
for coin in coins:
    for i in range(1, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]
print(dp[k])