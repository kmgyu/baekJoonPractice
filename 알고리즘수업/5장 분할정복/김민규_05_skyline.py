def skyline_pseudo(array):
    # 수도코드 기반 코드
    # 합병 정렬을 응용한 알고리즘. 합병 과정에서 차지하는 메모리를 조금씩 줄인다.
    # O(nlogn)의 시간복잡도를 가진다.
    # 백준에서 시간을 재보니 아래의 힙을 이용한 풀이보다 빨랐다.
    if len(array) == 1:
        return [[array[0][0], array[0][1]], [array[0][2], 0]]
    mid = len(array)//2
    ans = []
    # 분할
    left = skyline_pseudo(array[:mid])
    right = skyline_pseudo(array[mid:])
    
    # 합병 과정에서 keypoint 비교, 정렬과 함께 높이 비교. 필요없는 건 제거하며 공간 최적화
    l, r = 0,0 # two pointer
    l_h, r_h = 0,0 # left, right 높이
    currentx = 0 # 현재 x좌표
    l_len, r_len = len(left), len(right)
    while l<l_len and r<r_len:
        if left[l][0] < right[r][0]:
            currentx, l_h = left[l]
            l+=1
        elif left[l][0] > right[r][0]:
            currentx, r_h = right[r]
            r+=1
        else: # 좌표 같을 시 둘 다 내보내서 비교한다. 수도코드에는 없는 부분이었는데, 이 때문에 반례가 발생했었다.
            currentx, l_h = left[l]
            r_h = right[r][1]
            l+=1
            r+=1
        if not ans or max(l_h, r_h) != ans[-1][1]:
            # keypoint가 아무것도 존재하지 않거나, 높이가 다를 때만 추가.
            # 이렇게 안하면 각 사각형별로 겹치는 구간에서 point가 생성된다. 이런 중복데이터 방지용 if문
            ans.append([currentx, max(l_h, r_h)])
        # print(ans)
    # 남은거 붙이기
    ans += left[l:] + right[r:]
    return ans

from heapq import heappop, heappush
def skyline(data):
    n = len(data)
    # 힙을 이용한 다른 풀이. 분기문이 매우 많다. 위의 수도코드 기반 코드와 달리 공간 최적화가 없다.
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
    if stack[0][1] == 0: return stack[1:] #높이 0이면 슬라이싱해서 뱉는다.
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
print(skyline_pseudo(input3)) # [[1, 2], [2, 0]] 나와야함. 반례. 추가적인 코드 필요. 해결했다.


print(skyline(input1))
print(skyline(input2))
print(skyline(input3)) # 반례 해결. 그러나 이번엔 테스트 1, 2가 문제다... 해결했다.
