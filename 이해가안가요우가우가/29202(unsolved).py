# from itertools import combinations
from heapq import heappush, heappushpop
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = []
for i in range(n):
    w, v, t = map(int, input().split())
    bag.append((w,v,t,i+1))
bag.sort(key=lambda x: x[1]) # V_i 기준 정렬
# ans = 30e9+1
# books = []
# for i in combinations(bag, r=k):
#     s = sum([j[0] for j in i])
#     M = max([j[1] for j in i])
#     m = min([j[2] for j in i])
#     if ans >= s+M+m:
#         ans = s+M+m
#         books = [j[3] for j in i]

ans = float('inf')
books = []
for i in range(k, n):
    hq = []
    volume = bag[i][1] # V_i가 최댓값임.
    for j in range(i): # K-1개 유지하며 i 이전값들 대조
        # 가장 무거운 책을 앞으로 빼기
        if j >= k-1: # 허용 갯수 초과하면 빼고 넣기.
            heappushpop(hq, (-bag[j][0], bag[j]))
        else:
            heappush(hq, (-bag[j][0], bag[j])) 
    hq.append((0, bag[i]))
    
    weight = sum([hq[ii][1][0] for ii in range(k-1)])
    thick = min(hq, key = lambda x: x[1][2])[1][2]
    
    if ans > volume + weight + thick:
        ans = volume + weight + thick
        books = [hq[ii][1][3] for ii in range(k)]
        print(hq)
print(ans)
print(*books)