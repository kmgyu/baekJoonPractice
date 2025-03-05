import sys
input = sys.stdin.readline
n = int(input())
task = [list(map(int, input().split())) for _ in range(n)] +[0]
dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    if task[i][0]+i-1 > n-1:
        dp[i]=dp[i+1]
        continue
    dp[i] = max(task[i][1]+dp[i+task[i][0]], dp[i+1])
print(dp[0])