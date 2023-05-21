from math import gcd
n, s = map(int, input().split())
nums = [abs(i-s) for i in map(int,input().split())]
num = nums[0]
for i in range(1, n):
    num = gcd(num, nums[i])
print(num)