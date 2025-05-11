N = int(input())
nums = sorted(map(int, input().split()))

# https://www.acmicpc.net/board/view/45841
# what the...
if nums[0] > 1: print(1)
else:
    sums = nums[0]
    for i in range(1, N):
        if sums < nums[i]-1: # 연속되는 경우도 포함해야 한다.
            print(sums+1)
            break
        sums += nums[i]
    else: print(sums+1)