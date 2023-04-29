dp = [1, 1, 2]
n = int(input())
for i in range(3,n):
    dp.append(dp[-1]+dp[-2])
print(dp[n-1])