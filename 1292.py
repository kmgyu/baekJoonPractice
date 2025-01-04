nums = [0]
for i in range(1, 1001):
    nums += [i]*i
a, b = map(int, input().split())
print(sum(nums[a:b+1]))