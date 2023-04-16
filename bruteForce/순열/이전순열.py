n = int(input())
nums = list(map(int, input().split()))

def previous_permutation():
    i = n-1
    while i>0 and nums[i-1] <= nums[i]: i -= 1
    if i <= 0:
        print(-1)
        return
    
    j = n-1
    while nums[j] > nums[i-1]: j -= 1
    
    nums[i-1], nums[j] = nums[j], nums[i-1]
    j = n-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    print(*nums)

previous_permutation()
#다음순열코드의 원리에서 방향만 반대로했다.
#끼얏호우! 이번껀 내가 생각해서 조금만 고쳤다..