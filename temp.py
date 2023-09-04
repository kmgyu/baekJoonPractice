import sys
sys.setrecursionlimit(10**6)

def solve(n, x, y, cnt):
    row = (2**(n-1))-1
    column = (2**(n-1))-1
    
    for i in range(3):
        if 0 <= r-x <= row and 0 <= c-y <= column: break
        cnt += 2**((n-1)*2)
        x += dx[i]*(2**(n-1))
        y += dy[i]*(2**(n-1))
    
    if x == r and y == c:
        return cnt
    return solve(n-1, x, y, cnt)

dx = [0, 1, 0]
dy = [1, -1, 1]

n, r, c = map(int, input().split())
print(solve(n, 0, 0, 0))
