# 왜 안돌아가는거임;
# 딕셔너리 쓰면 안되나보다.
# 아니 vertex 번호도 내가 신경써줘야해????? 얼척이 없네
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stream = input().split()
    node = int(stream[0])
    edge_l = int(stream[1])

    edges = [set() for _ in range(node+1)]
    for i in range(1, edge_l+1):
        a, b = map(lambda x: int(x[1:]), stream[2*i:(2*i)+2])
        edges[a].add(b)
        edges[b].add(a)

    supervillain = int(stream[-1][1:])
    ans = 0
    # if supervillain in edges: