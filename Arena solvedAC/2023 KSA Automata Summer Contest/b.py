import sys
from math import gcd
def input(): return sys.stdin.readline()

n = int(input())
coor1 = set()
coor2 = set()
coor3 = set()
coor4 = set()
for i in range(n):
    a, b = map(int, input().split())
    p = gcd(a, b)
    a//=p
    b//=p
    if a>=0:
        if b>=0:coor1.add((a,b))
        else:coor4.add((a,b))
    else:
        if b>=0:coor2.add((a,b))
        else:coor3.add((a,b))
print(len(coor1)+len(coor2)+len(coor3)+len(coor4))