# https://codio.tistory.com/entry/%EB%B0%B1%EC%A4%80-1033%EB%B2%88-%EC%B9%B5%ED%85%8C%EC%9D%BC-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
from math import gcd
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(r):
    visited[r] = True
    for i in ratio[r]:
        if not visited[i[0]]:
            mass[i[0]] = i[2] * mass[r] // i[1]
            dfs(i[0])

n = int(input())
ratio = [[] for _ in range(n)]
mass = [0] * (n)
visited = [False] * n

multi = 1
for _ in range(n-1):
    a, b, p, q = map(int,input().split())
    ratio[a].append((b,p,q))
    ratio[b].append((a,q,p))
    multi *= ((p*q)//gcd(p,q))
mass[0] = multi

dfs(0)
##최대 공약수 구하기
maxGcd = mass[0]
for i in range(n):
    maxGcd = gcd(maxGcd,mass[i])

##최대공약수로 각 질량을 나눠줌
for i in range(len(mass)):
    mass[i] = mass[i] // maxGcd
print(*mass)