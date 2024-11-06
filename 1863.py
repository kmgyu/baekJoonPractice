import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y: stack.pop()

    if stack and y == stack[-1]: continue
    elif y>0:
        stack.append(y)
        ans += 1
        # print(stack, ans)
print(ans)
    
