n = int(input())
nums = list(map(int, input().split()))
isT = set()
for i in range(1, n):
    isT.add(nums[i]-nums[i-1])
if len(nums) > 2 and len(isT) != 1:
    print("NO")
    exit()
print("YES")
num1 = list(map(lambda x: x*2, nums))
num2 = list(map(lambda x: -x, nums))
print(*num1)
print(*num2)