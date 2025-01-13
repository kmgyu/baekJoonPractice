input = open(0).readline
N, M = map(int, input().split())
sq = [list(input()) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if sq[i][j] == '0': continue
        if i == 0 or j == 0:
            dp[i][j] = 1
            continue
        dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

print(max(max(row) for row in dp)**2)