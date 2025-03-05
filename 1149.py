from sys import stdin
input = stdin.readline
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(3):
        dp[i][j] += min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
print(min(*dp[-1]))