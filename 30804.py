input = open(0).readline
N=int(input())

# 구간 압축 방안도 존재
# right가 왼쪽부터 시작하는 투포인터. 머리를 잘... 아주 잘 굴려야 한다!
nums = [*map(int, input().split())]

bound = dict()

left, right, cnt = 0, 0, 0
answer = 0

while right < N:
    if (nums[right] not in bound) or (bound[nums[right]] == 0):
        bound[nums[right]] = 0
        cnt += 1
    bound[nums[right]] += 1
    
    while cnt > 2:
        bound[nums[left]] -= 1
        if (nums[left] not in bound) or (bound[nums[left]] == 0):
            cnt -= 1
        left += 1
    answer = max(answer, right-left+1)
    right += 1
print(answer)
