k = int(input())
nums = [list(map(int, input().split())) for _ in range(6)]
w = 0; w_idx = 0
h = 0; h_idx = 0
for i in range(6):
    if nums[i][0] <= 2:
        if w < nums[i][1]:
            w = nums[i][1]
            w_idx = i
    else:
        if h < nums[i][1]:
            h = nums[i][1]
            h_idx = i
#가장 긴 가로변 양옆 세로변들의 차이 : 뺄사각형 세로
#가장 긴 세로변 양옆 가로변들의 차이 : 뺄사각형 가로
subw = abs(nums[(w_idx-1)%6][1] - nums[(w_idx+1)%6][1])
subh = abs(nums[(h_idx-1)%6][1] - nums[(h_idx+1)%6][1])
print(((w*h) - (subw*subh)) * k)

# https://itcrowd2016.tistory.com/84