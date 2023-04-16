import sys

N = int(sys.stdin.readline().rstrip())

graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# for easy calculation assume node starts with 0 ~...
dp = [[-1] * (2**N) for _ in range(N)] # -1 if not searched yet
#2**N해주는 이유는 N*N의 행렬로 탐색을 해야하기 때문임. [시작노드][도착노드]이런식으로 연산해야해서... 여러개필요함.


def TSP(current_node, bitmask): # bitmask-> nodes which are already visited
    if bitmask | (0b1 << current_node) == (0b1 << N) -1:
        #현재 노드가 조사를 다 마쳤다면. (ob1 << N)으로 시프트연산할경우 11...11 이 됨.
        # 즉, 현재 조사한 노드에 대해 확인한다는 소리. 밑에서 저소리하는 이유가 설명됨.
        # current node is last node
        if graph[current_node][0] != 0: #갈수 있는 곳이라면?
            return graph[current_node][0]
        else:
            return int(2e9) #집 못가면 최댓값

    if dp[current_node][bitmask] != -1:
        return dp[current_node][bitmask]

    # else -> new -> should calculate
    ret = int(2e9)
    for i in range(N):
        if bitmask & (0b1 << i) or i == current_node or graph[current_node][i] == 0:
        #i가 시작지점과 같거나 i가 현재 노드거나 도달불가능할때 스킵
            continue
        #해당되지 않는 것 탐색
        tmp = TSP(i, bitmask | (0b1 << current_node))
        #최대 비용일때 스킵
        if tmp == int(2e9):
            continue
        #탐색의 최소비용 반환
        if ret > graph[current_node][i] + tmp:
            ret = graph[current_node][i] + tmp
    #현재 노드에서 시작점까지의 비용
    dp[current_node][bitmask] = ret

    return ret

print(TSP(0, 0))

# 다른사람꺼 돚거한 문제.
# import sys
# input=sys.stdin.readline
# n=int(input())
# W=[list(map(int,input().split())) for _ in range(n)]
# dp=[[-1]*(1<<n) for _ in range(n)]

# def city(last_city,route):
#     if route==(1<<n)-1:
#         if W[last_city][0]:
#             return W[last_city][0]
#         else:
#             return 17000000
#     if dp[last_city][route] != -1:
#         return dp[last_city][route]

#     dp[last_city][route]=17000000
#     for i in range(1,n):
#         if W[last_city][i] and route&(1<<i)==0:
#             price=city(i,route|(1<<i))
#             dp[last_city][route]=min(dp[last_city][route],W[last_city][i]+price)

#     return dp[last_city][route]

# minprice=city(0,1)
# print(minprice)