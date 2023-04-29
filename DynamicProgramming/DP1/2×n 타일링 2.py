n = int(input())
dp = [1, 3, 5]
for i in range(3, n):
    dp.append(dp[i-1]+dp[i-2]*2)
print((dp[n-1])%10007)