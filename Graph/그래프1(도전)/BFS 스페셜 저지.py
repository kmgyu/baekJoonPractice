from collections import deque
import sys
input = sys.stdin.readline

start = 1 # 시작점
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)] # 그래프 탐색여부
children = [set() for _ in range(N+1)] # 트리의 부모자식 관계
for _ in range(N-1): # 그래프 생성
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
test_case = list(map(int,input().split())) # 비교할 탐색 루트

# BFS, 부모 자식 관계 정립을 시킨다.
queue = deque()
queue.append(start)
visited[start] = 0
while queue:
    x = queue.popleft()
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1 # 방문처리
            children[x].add(i) # x의 자식은 i이다.
            queue.append(i)


next_index = 1
for i in test_case:
    if next_index == N:
        break
    c_length = len(children[i]) #자식의 길이
    c1 = set(test_case[next_index : next_index+c_length])
    c2 = children[i]
    if c1 != c2:
        print(0)
        exit()
    next_index += c_length
    # 부모 자식 관계 판별, 다음 인덱스로 넘어갈때마다 추가해줌
    # 다음 인덱스에서는 자식인덱스에만 접근하게 된다...
print(1)

# https://recordofwonseok.tistory.com/362