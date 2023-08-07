

stack = []

n = int(input())
index = 0
for i in range(n):
    s = input()
    if s == '?': index = i
    stack.append(s)

start = ""
end = ""
if index > 0:
    start = stack[index-1][-1]
if index < n-1:
    end = stack[index+1][0]
aa = set(stack)

m = int(input())
for i in range(m):
    s = input()
    if n == 1:
        print(s)
        exit()
    if s in aa: continue
    if index == n-1:
        if start == s[0]:
            print(s)
            exit()
    if index == 0:
        if end == s[-1]:
            print(s)
            exit()
    if 0 < index < n-1:
        if start == s[0] and end == s[-1]:
            print(s)
            exit()