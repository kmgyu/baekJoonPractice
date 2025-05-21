from collections import deque

for i in range(int(input())):
    s = deque(map(str, input()))
    ans = []
    cnt = 0
    while s:
        temp = s.popleft()
        if temp == '@':
            cnt += 1
            ans.append('a')
        elif temp == '[':
            cnt += 1
            ans.append('c')
        elif temp == '!':
            cnt += 1
            ans.append('i')
        elif temp == ';':
            cnt += 1
            ans.append('j')
        elif temp == '^':
            cnt += 1
            ans.append('n')
        elif temp == '0':
            cnt += 1
            ans.append('o')
        elif temp == '7':
            cnt += 1
            ans.append('t')
        elif temp == "'":
            if ans and ans[-1] == "\\":
                cnt += 1
                if len(ans) > 1 and ans[-2] == "\\":
                    ans.pop()
                    ans.pop()
                    ans.append('w')
                else:
                    ans.pop()
                    ans.append('v')
            else:
                ans.append(temp)
        else:
            ans.append(temp)
    if cnt >= len(ans)/2: print("I don't understand")
    else: print(*ans, sep="")