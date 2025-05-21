input = open(0).readline
size = int(input())
nums = list(map(int,input().strip().split()))
n = int(input())

def solve(size, nums, n):
    nums.sort()
    left,right=0,0
    for i in range(size+1):
        if nums[i] < n: left = nums[i]
        elif nums[i] > n: right = nums[i]
        else: return 0 # nums[i] == n
        if left < n < right: break
    left = n-left
    right = right-n
    return (left-1) * (right-1) + left-1 + right-1

print(solve(size, nums, n))