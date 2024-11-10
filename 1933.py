import sys
input = sys.stdin.readline 
def skyline(array):
    if len(array) == 1:
        return [[array[0][0], array[0][1]], [array[0][2], 0]]
    mid = len(array)//2
    ans = []
    left = skyline(array[:mid])
    right = skyline(array[mid:])
    
    l, r = 0,0
    l_h, r_h = 0,0
    currentx = 0
    while l<len(left) and r<len(right):
        if left[l][0] < right[r][0]:
            currentx, l_h = left[l]
            l+=1
        elif left[l][0] > right[r][0]:
            currentx, r_h = right[r]
            r+=1
        else:
            currentx, l_h = left[l]
            r_h = right[r][1]
            l+=1
            r+=1
        if not ans or max(l_h, r_h) != ans[-1][1]:
            ans.append([currentx, max(l_h, r_h)])
    ans += left[l:] + right[r:]
    return ans

n = int(input())
buildings = [list(map(int, input().split())) for _ in range(n)]

for b in skyline(buildings):
    print(*b, end=' ')