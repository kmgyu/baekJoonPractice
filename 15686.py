# bfs도 아니다.
# 맨해튼 거리를 이용해서 최소의 코스트 증가를 만들기
# 2의 값을 가진 노드를 제거하는 문제
# 치킨집(2 노드)는 M보다 큼이 보장되며, 13보다 작거나 같다.


N, M = map(int, input().split())
nodes = [[], []] # 0은 치킨집, 1은 집

for i in range(N):
    row = [*map(int, input().split())]
    for j in range(N):
        if row[j]: # 존재 시 좌표를 추가.
            # 2로 나눈 나머지. 2는 치킨집, 1은 집
            nodes[row[j]%2].append((i, j))

chicks = len(nodes[0]) # 치킨집 개수

chick_dist = dict()

def calc(houses):
    # 치킨집(houses)에 대한 맨해튼 거리 계산
    c_dict = dict()
    for node in nodes[1]:
        for house in houses:
            dist = abs(node[0]-house[0])+abs(node[1]-house[1])
            if node not in c_dict: c_dict[node]=float('inf')
            c_dict[node] = min(dist, c_dict[node]) # 최소값 갱신
    return sum(c_dict.values()) # 거리 합(=치킨 거리) 반환

def dfs(index, houses, cnt):
    if index==chicks and cnt == M:
        return calc(houses)
    
    result = float('inf')
    if index < chicks:
        if cnt < M:
            result = min(dfs(index+1, houses+[nodes[0][index]], cnt+1), result)
        result = min(dfs(index+1, houses, cnt), result)
    return result

print(dfs(0, [], 0))