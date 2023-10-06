import sys
input=lambda:sys.stdin.readline().rstrip() # input 호출시 해당 함수와 같다.

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

v, e = map(int, input().split())

node = list(range(v+1)) # 리스트는 자신의 부모를 가리킴. 
weight = [tuple(map(int, input().split())) for _ in range(e)]
weight.sort(key=lambda x:x[2])
# 모든 간선의 정보 리스트, 크루스칼 알고리즘을 위해 가중치 정렬

answer = 0 # 출력(트리의 가중치)
for i in weight:
    if union(i[0], i[1]): # 참인 경우에만 간선의 가중치 추가
        answer += i[2]
print(answer)