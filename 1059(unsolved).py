import sys
input = sys.stdin.readline
size = int(input())
nums = list(map(int,input().strip().split()))
n = int(input())

def solve(size, nums, n):
    nums.sort()
    left, right=0,0
    for i in range(size+1):
        if nums[i]>n:
            left=nums[i-1]+1
            right=nums[i]-1
            break
        if nums[i]==n:
            return 0

    return (n-left) * (right-n+1) + (right-n)

print(solve(size, nums, n))