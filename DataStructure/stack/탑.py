# referenced
# https://velog.io/@ckstn0777/%EB%B0%B1%EC%A4%80-22866%EB%B2%88-%ED%83%91-%EB%B3%B4%EA%B8%B0

n = int(input())
l = list(map(int, input().split()))

cnt = [0] * (n+1)
near = [[int(1e9), int(1e9)] for _ in range(n + 1)]

stack = []
for idx, v in enumerate(l, 1):
    while len(stack) > 0 and stack[-1][1] <= v:
        stack.pop()
    cnt[idx] += len(stack)
    
    if len(stack) > 0:
        dist = abs(stack[-1][0] - idx)
        if dist < near[idx][1]:
            near[idx][0] = stack[-1][0]
            near[idx][1] = dist
    stack.append([idx, v])

stack = []
for idx, v in reversed(list(enumerate(l, 1))):
    while len(stack) > 0 and stack[-1][1] <= v:
        stack.pop()
    cnt[idx] += len(stack)
    
    if len(stack) > 0:
        dist = abs(stack[-1][0] - idx)
        if dist < near[idx][1]:
            near[idx][0] = stack[-1][0]
            near[idx][1] = dist
        elif dist == near[idx][1] and stack[-1][0] < near[idx][0]:
            near[idx][0] = stack[-1][0]
    stack.append([idx, v])

for i in range(1, n+1):
    if cnt[i] > 0:
        print(f"{cnt[i]} {near[i][0]}")
    else:
        print(0)