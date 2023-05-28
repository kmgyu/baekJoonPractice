n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [0]*(n+1)
dp[1] = nums[0]
if n > 1: dp[2] = max(nums[0]+nums[1], nums[1])
if n > 2: dp[3] = max(nums[0]+nums[2], nums[1]+nums[2])
for i in range(4, n+1):
    dp[i] = max(nums[i-1]+dp[i-3]+nums[i-2], nums[i-1]+dp[i-2])
print(dp[n])