n = int(input())
nums = list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = nums[i-1] + dp[i-1]
print(dp)

#길이 구하고 그거의 합구하는거임! 최고합!