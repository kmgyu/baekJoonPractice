from sys import stdin
input = stdin.readline
br1 = ['(', '[']
br2 = [')', ']']

def finder(string):
    s = string
    stack = []
    for i in s:
        if i in br1:
            stack.append(i)
        if i in br2:
            if stack:
                temp = stack.pop()
            else:
                print("no")
                return
            if temp == '(' and i ==']' or temp =='[' and i ==')':
                print("no")
                return
    if stack:
        print("no")
    else:
        print("yes")

while True:
    s = input().rstrip()
    if s == '.':
        break
    finder(s)
