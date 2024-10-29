import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

visited=[False]*(n+1)
distance=[int(1e9)]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    for i in graph[a]:
        if i[0] == b:
            i[1] = min(i[1],c)
            break
    else:
        graph[a].append([b,c])


def get_smallest_node():
    min_value=int(1e9)
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 처리된적이 있는 노드라면 pass
        if distance[now]<dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])