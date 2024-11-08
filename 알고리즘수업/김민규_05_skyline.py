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
                if stack and h != stack[-1][1]: # 높이 다르면 추가
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
        stack.append((l,h))
        end = r
    stack.append((end,0))
    return stack

from queue import PriorityQueue

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # Initialize the skyline results array, a list to store building edges,
        # and a priority queue to manage the current highest buildings
        skyline = []
        edges = []
        max_heights = PriorityQueue()
      
        # Create a sorted list of all critical points (building start and end)
        for building in buildings:
            edges.extend([building[0], building[1]])
        edges.sort()
      
        # Initialize pointers and get the total number of buildings
        building_index, total_buildings = 0, len(buildings)

        # Process each edge in the sorted list to determine skyline changes
        for edge in edges:
            # Add buildings to the priority queue which start before or at the current edge
            while building_index < total_buildings and buildings[building_index][0] <= edge:
                # Insert into the priority queue the negative height (to reverse the default order),
                # the start, and the end of the current building
                max_heights.put([-buildings[building_index][2], buildings[building_index][1]])
                building_index += 1
          
            # Remove buildings from priority queue which end before the current edge
            while not max_heights.empty() and max_heights.queue[0][1] <= edge:
                max_heights.get()

            # The height is 0 if there are no buildings in sight, or the highest if there are
            height = -max_heights.queue[0][0] if not max_heights.empty() else 0
          
            # Only add a point to the skyline if the height changes from the last point
            if not skyline or skyline[-1][1] != height:
                skyline.append([edge, height])
      
        return skyline

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
print(skyline(input3)) # 반례 해결. 그러나 이번엔 테스트 1, 2가 문제다...

print(Solution().getSkyline(input1))
print(Solution().getSkyline(input2))
print(Solution().getSkyline(input3))