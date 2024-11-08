def skyline_pseudo(array):
    # 수도코드를 그대로 작성했다.
    # 합병 정렬을 응용한 알고리즘. 합병 과정에서 차지하는 메모리를 조금씩 줄인다.
    # O(nlogn)의 시간복잡도를 가진다.
    if len(array) == 1:
        return [[array[0][0], array[0][1]], [array[0][2], 0]]
    mid = len(array)//2
    ans = []
    left = skyline_pseudo(array[:mid])
    right = skyline_pseudo(array[mid:])
    
    left_pointer = 0
    right_pointer = 0
    currentx = 0
    while left and right:
        # print(left[0], right[0])
        if left[0][0] < right[0][0]:
            currentx = left[0][0]
            left_pointer = left[0][1]
            left.pop(0)
        else:
            currentx = right[0][0]
            right_pointer = right[0][1]
            right.pop(0)
        if not ans or max(left_pointer, right_pointer) != ans[-1][1]:
            # keypoint가 아무것도 존재하지 않거나, 높이가 다를 때만 추가.
            # 이렇게 안하면 각 사각형별로 겹치는 구간에서 point가 생성된다. 이런 중복데이터 방지용 if문
            ans.append([currentx, max(left_pointer, right_pointer)])
        # print(ans)
    if not left: ans += right
    else: ans += left
    return ans

from heapq import heappop, heappush
def skyline(data):
    n = len(data)
    # 반례 해결을 위해 추가적으로 자료를 찾아봄.
    # 힙을 이용한... 분할 정복...?
    # 단점 : 0,0 무조건 추가함
    buildings = []
    for i in data:
        heappush(buildings, i)

    stack = []
    end = 0
    while buildings:
        l,h,r = heappop(buildings)
        if l >= end:
            if l > end: # 건물 끊어지면 각각 추가
                stack.append((end,0))
                stack.append((l,h))
            else: # 건물 연장
                if not stack or h != stack[-1][1]: # 높이 다르면 추가
                    stack.append((l,h))
            end = r
            continue
        if stack and h <= stack[-1][1]:
            if r > end: # 높이가 더 낮은데 끝이 긴 경우 end~r로 잘라서 추가
                heappush(buildings,[end,h,r])
            continue
        if end > r: # 높이 크고 끝이 짧은 경우 r~end로 잘라서 추가
            heappush(buildings,[r,stack[-1][1],end])
        if stack and l == stack[-1][0]: # x가 같으면 pop
            stack.pop()
        stack.append((l,h)) # 조건분기 다끝내면 최종적으로 l을 추가해줌.
        end = r
    stack.append((end,0))
    if stack[0][0] == 0: return stack[1:] #높이 0이면 슬라이싱해서 뱉는다.
    return stack



# test driver
# start, height, end
input1 = [[0, 5, 9], [1, 3, 13], [11, 4, 18], [15, 7, 23], 
[27, 2, 35],[30, 3, 40], [38, 6, 48], [42, 10, 55], 
[43, 2, 53]]
input2 =  [[2, 10, 9], [3, 15, 7], [5, 12, 12], [15, 10, 20], 
[19, 8, 24]]
input3 = [[1,1,2], [1, 2, 2]]
print(skyline_pseudo(input1))
print(skyline_pseudo(input2))
print(skyline_pseudo(input3)) # [[1, 2], [2, 0]] 나와야함. 반례. 추가적인 코드 필요


print(skyline(input1))
print(skyline(input2))
print(skyline(input3)) # 반례 해결. 그러나 이번엔 테스트 1, 2가 문제다... 해결했다.
