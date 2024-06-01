import sys
from heapq import heappush, heappop
from collections import deque, defaultdict

input = sys.stdin.readline
inf = float('inf')

def bfs(start, n, graph):
    """
    너비 우선 탐색(BFS) 알고리즘을 사용하여 시작 노드에서부터
    각 노드까지의 최단 거리를 계산합니다.
    
    :param start: 시작 노드
    :param n: 노드의 개수
    :param graph: 그래프 (인접 리스트 형태)
    :return: 시작 노드에서부터 각 노드까지의 최단 거리를 나타내는 리스트
    """
    dist = [inf] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor, _ in graph[node]:
            if dist[neighbor] == inf:  # Not visited
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist

def find_hanbyul_path(b, c, bfs_dist, graph, edge_cnt):
    """
    한별 선배의 집부터 학교까지의 경로를 찾습니다.
    
    :param b: 한별 선배의 집
    :param c: 학교
    :param bfs_dist: BFS를 통해 구한 각 노드까지의 최단 거리
    :param graph: 그래프 (인접 리스트 형태)
    :param edge_cnt: 각 노드의 연결된 간선 수
    :return: 한별 선배의 집부터 학교까지의 경로를 나타내는 리스트
    """
    path = []
    current = b
    while current != c:
        path.append(current)
        neighbors = graph[current]
        neighbors.sort(key=lambda x: (-edge_cnt[x[0]], -x[0]))
        for neighbor, _ in neighbors:
            if bfs_dist[neighbor] == bfs_dist[current] - 1:
                current = neighbor
                break
    path.append(c)
    return path

def dijkstra(start, n, graph):
    """
    다익스트라 알고리즘을 사용하여 시작 노드에서부터 각 노드까지의 최단 거리를 계산합니다.
    
    :param start: 시작 노드
    :param n: 노드의 개수
    :param graph: 그래프 (인접 리스트 형태)
    :return: 시작 노드에서부터 각 노드까지의 최단 거리를 나타내는 리스트
    """
    dist = [inf] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, node = heappop(heap)
        if d > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(heap, (new_dist, neighbor))
    
    return dist

# 입력 처리
n, m = map(int, input().split())
a, b, c = map(int, input().split())

graph = defaultdict(list)
edge_cnt = defaultdict(int)

for _ in range(m):
    i, j, k = map(int, input().split())
    graph[i].append((j, k))
    graph[j].append((i, k))
    edge_cnt[i] += 1
    edge_cnt[j] += 1
    
# 1. 학교에서 BFS 수행
bfs_dist = bfs(c, n, graph)

# 2. 한별 선배의 경로 찾기
hanbyul_path = find_hanbyul_path(b, c, bfs_dist, graph, edge_cnt)

# 3. 토카의 최단 경로 찾기 (다익스트라)
dist_from_a = dijkstra(a, n, graph)

# 4. 한별 선배의 경로 중에서 토카가 가장 빨리 도착할 수 있는 지점 찾기
best_meeting_point = (inf, inf)

for node in hanbyul_path:
    if dist_from_a[node] < best_meeting_point[0] or (dist_from_a[node] == best_meeting_point[0] and node < best_meeting_point[1]):
        best_meeting_point = (dist_from_a[node], node)

print(best_meeting_point[1])
