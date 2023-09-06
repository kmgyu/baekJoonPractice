t = int(input())
nums = []
for i in range(t):
    nums.append(int(input()))
n = max(nums)

dp = [0, 1, 1]
for i in range(2, n):
    dp.append(dp[-3]+dp[-2])
for i in nums:
    print(dp[i])
