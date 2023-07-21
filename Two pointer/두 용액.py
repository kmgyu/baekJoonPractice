import sys
input = sys.stdin.readline
n = int(input())
num = sorted(map(int, input().split()))
right = n-1
left = 0
ans = 10e9
tr = right
tl = left
while tl < tr:
    if ans >= abs(num[tr] + num[tl]):
        ans = abs(num[tr] + num[tl])
        right = tr
        left = tl
        if ans == 0:
            break
    if num[tr] + num[tl] > 0:
        tr -= 1
    elif num[tr] + num[tl] < 0:
        tl += 1
print(num[left], num[right])