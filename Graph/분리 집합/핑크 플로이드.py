import sys
input = sys.stdin.readline

def find(n):
    if n != node[n]:
        node[n] = find(node[n])
        #find 메소드로 노드를 연결시키고 반환 할 시, 재귀를 여러번 거치지 않을 수 있다. 공통 조상 노드로 연결되기 때문.
        return node[n]
    return n

def union(a, b): # 부모 자식 관계 통일 메소드, union-find 알고리즘
    parent = find(a) # 부모(예정)
    child = find(b) # 자식(예정)
    if parent>child: parent, child = child, parent # 간선을 이을 때는 인덱스 값 낮은 쪽이 부모.
    if parent != child: # 만약, 서로의 부모가 다를 경우
        node[child] = parent # 자식쪽에서 부모의 인덱스를 가리킴
        return True # 참 반환
    return False # 부모가 같을 경우, 거짓 반환.

n = int(input())
edge = []
node = list(range(n))


for i in range(n-1):
    tmp = list(map(int, input().split()))
    for j in range(i+1, n):
        edge.append((i, j, tmp[j-i-1]))
edge.sort(key = lambda x: x[2])

graph = [[] for _ in range(n)]

cnt = [0] * n
for i in edge:
    if union(i[0], i[1]): # 참인 경우에만 간선의 가중치 추가
        graph[i[0]].append(i[1]+1)
        graph[i[1]].append(i[0]+1)
        cnt[i[0]] += 1
        cnt[i[1]] += 1

for i in range(n):
    print(cnt[i], *sorted(graph[i]))