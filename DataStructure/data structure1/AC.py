from collections import deque
from sys import stdin
input = stdin.readline
t = int(input()) #testcase

def ac(func, li):
    r = 1 # if r(everse)is 1, popleft
    for j in func:
        if j == 'R':
            r *= -1
        elif j == 'D':
            if len(li) == 0:
                print("error")
                return
            if r == 1:
                li.popleft()
            else:
                li.pop()
    li = list(li)
    if r == -1:
        li.reverse()
    print("["+",".join(map(str,li))+"]")
for _ in range(t):
    func = input().strip() #R reverse D pop
    leng = int(input().strip()) #length
    temp = input().strip()[1:-1]
    li = deque()
    if temp:
        li = deque(temp.split(","))
    ac(func, li)