from bisect import bisect_right

def dfs(lst, sum, target, end_p):
    if target != end_p:
        lst.append(sum + nums[target])
        dfs(lst, sum + nums[target], target + 1, end_p)
        dfs(lst, sum, target + 1, end_p)

def solve(target1, target2, bound):
    cnt = 0
    for i in target1:
        cnt += bisect_right(target2, bound-i)
    return cnt

# example
nums = list(range(1, 10))
nums1=[0]
nums2=[0]

# 연관 문제 1208, 1450
# 리스트 반갈죽하고 이분탐색 인덱스로 경우의 수를 더하는 간단한 문제...
# 응용하면 더 어려워질 것이다...
# 2^N보다 2^(N//2)로 풀이하는 전략이라고 한다...? 사실 잘 모른다. 어려워...
# https://killerwhale0917.tistory.com/5
# n**m을 2*n**m-1 로 줄여주는 연산이라곻 한다.