from sys import stdin
input = stdin.readline
while True:
    inner = list(map(int,input().split()))
    n = inner[0]
    if n == 0:
        break
    nums = [0] + inner[1:] + [0]
    s = [0]
    ans = 0
    for i in range(1, n+2):
        while s and nums[s[-1]] > nums[i]:
            check = s.pop()
            ans = max(ans, nums[check]*(i-s[-1]-1))
        s.append(i)
    print(ans)
