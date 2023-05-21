from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0]
for i in range(n):
    dp.append(nums[i]+dp[-1])
ans = -10e9
for i in range(k, n+1):
    ans = max(ans, dp[i]-dp[i-k])
print(ans)
