from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]

start, end = min(time), max(time)*m
ans = end
while start <= end:
    mid = (start+end)//2
    man = 0
    for i in time:
        man += mid//i
    if man >= m:
        end = mid-1
        ans = min(ans, mid)
    else:
        start = mid+1
print(ans)