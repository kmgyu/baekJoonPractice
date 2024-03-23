import sys
input = sys.stdin.readline

n, k, s = map(int, input().split())
left = []
right = []

for i in range(n):
    a, b = map(int, input().split())
    if a-s < 0:
        left.append([s-a, b])
    else:
        right.append([a-s, b])

left.sort(); right.sort()

ans = 0
while left:
    if left[-1][1] <= 0:
        left.pop()
        continue
    left[-1][1] -= k
    ans += left[-1][0]*2
    while len(left)>1 and left[-1][1] <= 0:
        left[-2][1] += left[-1][1]
        left.pop()

while right:
    if right[-1][1] <= 0:
        right.pop()
        continue
    right[-1][1] -= k
    ans += right[-1][0]*2
    while len(right)>1 and right[-1][1] <= 0:
        right[-2][1] += right[-1][1]
        right.pop()

print(ans)