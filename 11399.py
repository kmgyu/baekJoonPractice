n = int(input())
time = list(map(int, input().split()))
stack = [0]
time.sort()
for i in time:
    stack.append(stack[-1]+i)
print(sum(stack))