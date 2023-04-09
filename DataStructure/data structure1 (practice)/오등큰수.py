from collections import Counter
n = int(input())
num = list(map(int, input().split()))
count = Counter(num)
stack = []
ans = [-1] * n
for i in range(len(num)):
    if len(stack) != 0:
        while stack and count[num[stack[-1]]] < count[num[i]]:
            ans[stack.pop()] = num[i]
    stack.append(i)
print(*ans)