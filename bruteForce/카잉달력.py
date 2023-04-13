from sys import stdin
from math import lcm
input = stdin.readline
t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    j, k = (x, x)
    
    cnt = x % (m+1)
    tempY = x;
    for i in range(n):
        ty = tempY%n
        if ty == 0:
            ty = n
        if ty == y:
            break
        tempY = ty + m
        cnt +=m
    if cnt > lcm(m,n):
        print(-1)
    else:
        print(cnt)

#x에 m을 계속 더해가면서 count하고, 같은 값이 나오는지 확인
#그거 출력하면됨.
#그런데 최소공배수까지가서 안나오면 컷