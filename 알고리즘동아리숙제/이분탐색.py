import random
nums = sorted([random.randrange(1,100) for _ in range(20)])

def binSearch(left, right, n):
    mid = (left+right)//2
    ans = 0
    if left > right:
        return "can't find anything here"
    
    if nums[mid] == n:
        return mid
    elif nums[mid] < n:
        left = mid+1
        ans = binSearch(left, right, n)
    else: #nums[mid] < n
        right = mid-1
        ans = binSearch(left, right, n)
    return ans

print(binSearch(0, len(nums), int(input())))
print(*nums, sep=", ")