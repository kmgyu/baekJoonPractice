from sys import stdin
input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [[0] for _ in range(2)]
dp[0][0] = nums[0]
dp[1][0] = -10e9
ans = nums[0]
for i in range(1, n):
    dp[0].append(max(dp[0][i-1]+nums[i], nums[i]))
    dp[1].append(max(dp[0][i-1], dp[1][i-1]+nums[i]))
    ans = max(dp[0][i], dp[1][i], ans)
print(ans)
# https://seol-limit.tistory.com/46