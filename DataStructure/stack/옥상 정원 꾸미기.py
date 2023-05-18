from sys import stdin
input = stdin.readline
n=int(input())
mount = []
for i in range(n):
    mount.append(int(input()))
stack = []
ans = 0
for i in range(n):
    temp = mount[i]
    while len(stack) > 0 and temp > stack[-1]:
        stack.pop()
    ans += len(stack)
    stack.append(temp)
print(ans)
# cnt=0
# for i in range(n):
#     m = mount[i]
#     j = i+1
#     while j < n and mount[j] < m:
#         cnt+=1
#         j+=1
# print(cnt)