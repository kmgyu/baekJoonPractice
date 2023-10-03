n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]
for i in range(1, n):
    dp.append(dp[-1]+nums[i])
res = []
#bucket right
ans = 0
for i in range(1, n-1):
    ans = max(ans, dp[-1]*2-dp[i]-nums[0]-nums[i])
res.append(ans)
#bucket left
ans = 0
for i in range(1, n-1):
    ans = max(ans, dp[i-1]+dp[-1]-nums[i]-nums[-1])
res.append(ans)
#bucket middle
ans = 0
for i in range(1, n-1):
    ans = max(ans, dp[i]-nums[0] + dp[-1]-dp[i-1]-nums[-1])
res.append(ans)
print(max(res))
