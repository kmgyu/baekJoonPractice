s = list(input())
stack = []
for i in range(len(s)):
    temp = s[i]
    if stack:
        if stack[-1] == 'A' and temp == 'P':
            stack.pop()
            for _ in range(2):
                if stack:
                    if stack[-1] == 'P':
                        stack.pop()
                    else:print("NP");exit()
                else:
                    print("NP")
                    exit()
    stack.append(temp)
if len(stack) == 1 and stack[0] == 'P':
    print("PPAP")
else:
    print("NP")