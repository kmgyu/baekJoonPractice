import sys
input = open(0).readline
#오버헤드 줄이기 갈라쇼
def solve(array):
    if len(array) == 1:
        return [(array[0][0], array[0][1]), (array[0][2], 0)]
    mid = len(array)//2
    left = solve(array[:mid])
    right = solve(array[mid:])
    return merge(left, right)
    
def merge(left, right):
    ans = []
    l, r = 0,0
    l_h, r_h = 0,0
    currentx = 0
    l_len, r_len = len(left), len(right)
    while l<l_len and r<r_len:
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
        m_h = max(l_h, r_h)
        if not ans or m_h != ans[-1][1]:
            ans.append((currentx, m_h))
    if l < l_len:ans += left[l:]
    else: ans+= right[r:]
    return ans

n = int(input())
buildings = [list(map(int, input().split())) for _ in range(n)]

print = sys.stdout.write
for b in solve(buildings):
    print(f'{b[0]} {b[1]} ')