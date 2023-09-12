def solve(t):
    n = t
    dp = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(1, n+1, i):
            dp[i] += 1
    print(*dp)
    print(n, "=", sum(dp))

for i in range(1, 20):
    solve(i)