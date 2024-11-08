import sys
input = sys.stdin.readline 

from collections import deque
def skyline(start, end):
    if end-start == 1:
        return deque([[buildings[start][0], buildings[start][1]], [buildings[start][2], 0]])
    mid = (start+end)//2
    
    # stack = []
    # end = 0
    # while buildings:
    #     l,h,r = heappop(buildings)
    #     if l >= end:
    #         if l > end:
    #             stack.append((end,0))
    #             stack.append((l,h))
    #         else:
    #             if h != stack[-1][1]:
    #                 stack.append((l,h))
    #         end = r
    #         continue
    #     if h <= stack[-1][1]:
    #         if r > end:
    #             heappush(buildings,[end,h,r])
    #         continue
    #     if end > r:
    #         heappush(buildings,[r,stack[-1][1],end])
    #     if l == stack[-1][0]:
    #         stack.pop()
    #     stack.append((l,h))
    #     end = r
    # stack.append((end,0))
    
    ans = deque()
    left = skyline(start, mid)
    right = skyline(mid, end)
    currentx = 0
    l_pointer = 0
    r_pointer = 0
    while left and right:
        if left[0][0] < right[0][0]:
            currentx, l_pointer = left.popleft()
        else:
            currentx, r_pointer = right.popleft()
        if not ans or (max(l_pointer, r_pointer) != ans[-1][1] and currentx != ans[-1][0]):
            ans.append([currentx, max(l_pointer, r_pointer)])
    if not left:
        while right:
            r = right.popleft()
            if r[0] > ans[-1][0]:
                ans.append(r)
    else:
        while left:
            l = left.popleft()
            if l[0] > ans[-1][0]:
                ans.append(l)
    return ans


n = int(input())
buildings = [list(map(int, input().split())) for _ in range(n)]
ans = skyline(0, n)

print(*ans, end=' ')
