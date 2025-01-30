input = open(0).readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

cur_cost = cost[0]
cur_dist = 0
result = 0
for i in range(1, N):
    cur_dist += dist[i-1]
    if cost[i] < cur_cost:
        result += cur_dist * cur_cost
        cur_dist = 0
        cur_cost = cost[i]

if cur_dist:
    result += cur_dist * cur_cost
        
print(result)