import sys
input = sys.stdin.readline

def solve(x1, y1, x2, y2):
    global h, w
    if (x1 + x2 <= h and max(y1, y2) <= w) or (max(x1, x2) <= h and y1 + y2 <= w):
        return x1*y1 + x2*y2
    return 0

h, w = map(int, input().split())
n = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = stickers[i]
        x2, y2 = stickers[j]
        result = max(solve(x1, y1, x2, y2),
                     solve(x1, y1, y2, x2),
                     solve(y1, x1, y2, x2),
                     solve(y1, x1, x2, y2),
                     result
                     )
print(result)