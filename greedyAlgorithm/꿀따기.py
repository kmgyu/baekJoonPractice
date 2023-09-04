n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]
for i in range(1, n):
    dp.append(dp[-1]+nums[i])
res = []
ans = 0
for i in range(1, n-1):
    ans = max(ans, dp[-1]*2-dp[i]-nums[0]-nums[i], dp[i-1]+dp[-1]-nums[i]-nums[-1], dp[i]-nums[0] + dp[-1]-dp[i-1]-nums[-1])
print(ans)
