from sys import stdin
input = stdin.readline
n = int(input()) #triangle scale
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
dp = [[0]*i for i in range(1, n+1)]
dp[0][0] = nums[0][0]

for i in range(1, n):
    for j in range(i):
        dp[i][j] = max(nums[i][j] + dp[i-1][j], dp[i][j])
        dp[i][j+1] = nums[i][j+1] + dp[i-1][j]

print(max(dp[-1]))