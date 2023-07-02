from sys import stdin
input = stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
cnt = 0
stack = [[nums[0], 1]]
for h in nums[1:]:
    cur_h = stack[-1][0]
    now_h = h
    man = 1
    if now_h < cur_h:
        cnt += 1
    elif now_h == cur_h:
        stack[-1] = [stack[-1][0], stack[-1][1]+1]
        if len(stack) > 1:
            cnt += stack[-1][1]
        else:
            cnt += stack[-1][1] - 1
        continue
    else:
        while stack:
            if stack[-1][0] < h and man == 1:
                cnt += stack.pop()[1]
            elif stack[-1][0] == h:
                tmp_h, tmp_m = stack.pop()
                cnt += tmp_m
                man += tmp_m
            else:
                cnt+=1
                break
    stack.append([h, man])
print(cnt)