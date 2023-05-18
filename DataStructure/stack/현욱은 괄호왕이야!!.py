n = int(input())
s = input()
stack = []
result = []
for i in range(len(s)):
    temp = i
    if stack and s[stack[-1]] == '(' and s[temp] == ')':
        stack.pop()
    else:
        stack.append(temp)
cur = 0
for i in stack:
    if not result:
        result.append(i)
    else:
        result.append(i-cur-1)
    cur = i
if stack:
    result.append(n-stack[-1]-1)
if not stack:
    result.append(n)
print(max(result))