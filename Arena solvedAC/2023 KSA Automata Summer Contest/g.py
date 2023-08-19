from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = []
for i in range(n):
    w, v, t = map(int, input().split())
    bag.append((w,v,t,i+1))
ans = 30e9+1
books = []
for i in combinations(bag, r=k):
    s = sum([j[0] for j in i])
    M = max([j[1] for j in i])
    m = min([j[2] for j in i])
    if ans >= s+M+m:
        ans = s+M+m
        books = [j[3] for j in i]
print(ans)
print(*books)