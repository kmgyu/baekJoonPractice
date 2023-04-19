import sys

input = sys.stdin.readline
n = int(input())
stk = list()
for i in range(0, n):
    s = input().split()
    sl = len(stk)
    if s[0] == "push":
        stk.append(s[1])
    elif s[0] == "pop":
        if sl:
            print(stk[sl-1])
            stk.pop()
        else:
            print(-1)
    elif s[0] == "size":
        print(sl)
    elif s[0] == "empty":
        if sl:
            print(0)
        else:
            print(1)
    elif s[0] == "top":
        if sl:
            print(stk[sl-1])
        else:
            print(-1)





