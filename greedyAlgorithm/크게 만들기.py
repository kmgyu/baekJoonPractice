from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().rstrip()))
ans = []
cnt = 0
for i in range(n):
    temp = nums[i]
    if ans:
        while ans and ans[-1] < temp and cnt < k:
            ans.pop()
            cnt+=1
    ans.append(temp)
while cnt < k:
    ans.pop()
    cnt+=1
print(*ans,sep="")