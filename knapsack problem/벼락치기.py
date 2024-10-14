# 29704
n, t = map(int, input().split())

dp = [0] * (t+1)
# dp[0] = 0
a=0
for _ in range(n):
    d, m = map(int, input().split())
    a+=m
    for j in range(t, 0, -1):
        if j >= d:
            dp[j] = max(dp[j], dp[j-d] + m)

print(a-dp[-1])