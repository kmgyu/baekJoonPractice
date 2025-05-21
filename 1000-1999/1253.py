import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int, input().split()))

length = len(nums)

cnt = 0
for i in range(n):
    num = nums[i]
    l = 0
    r = length-1
    while l < r:
        if nums[l] + nums[r] == num:
            if r == i:
                r -= 1
                continue
            elif l == i:
                l += 1
                continue
            cnt += 1
            break
        if nums[l] + nums[r] > num:
            r -= 1
        else:
            l += 1

print(cnt)