from collections import deque
import sys
input = sys.stdin.readline

# pypy3 성공, python3 실패. 제한적 성공

def d(num):
    return (num*2)%10000

def s(num):
    if num==0: return 9999
    return num-1

def r(num):
    n123 = num//10
    n4 = num%10
    return n4*1000 + n123

def l(num):
    n1 = num//1000
    n234 = num%1000
    
    return n234*10 + n1

def search(cur, target):
    q = deque()
    q.append([cur, ""])
    
    strs = ["D", "S", "L", "R"]
    funcs = (d, s, l, r)
    visited = set()
    
    while q:
        cur_num, log = q.popleft()
        for i in range(4):
            tmp = funcs[i](cur_num)
            if tmp in visited: continue
            if tmp == target:
                return log+strs[i]
            q.append((tmp, log+strs[i]))
            visited.add(tmp)


for i in range(int(input())):
    a, b = map(int, input().split())
    print(search(a, b))