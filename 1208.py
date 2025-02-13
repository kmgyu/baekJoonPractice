# 1450이랑 비슷한 문제
# https://killerwhale0917.tistory.com/5
# 머리를 두번 써야 한다.
from bisect import bisect_right, bisect_left

def dfs(lst, sum, target, end_p):
    if target != end_p:
        lst.append(sum + nums[target])
        dfs(lst, sum + nums[target], target + 1, end_p)
        dfs(lst, sum, target + 1, end_p)

def solve(target1, target2, bound):
    cnt = 0
    for i in target1:
        cnt += bisect_right(target2, bound-i) - bisect_left(target2, bound-i)
        # 음의 정수 ~ 양의 정수이므로 충족되는 인덱스를 두번 조회해서 바운더리 구성해야 한다.
    return cnt

N, S = map(int, input().split())
nums = list(map(int, input().split()))
nums1 = []
nums2 = []

dfs(nums1, 0, 0, N//2)
dfs(nums2, 0, N//2, N)
nums1.sort()
nums2.sort()
# print(nums1, nums2, sep="\n")

# 내부에서 수열 성립되는 거 더해줘야 함. nums1의 요소 하나 하나도 수열이니까...
i1 = bisect_right(nums1, S) - bisect_left(nums1, S) 
i2 = bisect_right(nums2, S) - bisect_left(nums2, S)
print(solve(nums1, nums2, S) + i1 + i2)
