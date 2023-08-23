n = int(input())
nums = list(map(int, input().split()))
dp = []
for i in range(1, n):
    dp.append((nums[i-1]^nums[i]) - (nums[i-1]+nums[i]))
su = 0
tmp = 0
for i in range(n-1):
    pass