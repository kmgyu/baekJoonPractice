# 데이크스트라 + BFS

from collections import deque

n, k = map(int, input().split())
visitied = [0] * 100001
q = deque()
q.append(n)
while q:
    node = q.popleft()
    if node == k:
        print(visitied[k])
        break
    for next_n in (node+1, node-1, node*2):
        if 0 <= next_n < 100001:
            if visitied[next_n] == 0:
                if next_n == node*2 and next_n != 0:
                    visitied[next_n] = visitied[node]
                    q.appendleft(next_n)
                else:
                    visitied[next_n] = visitied[node] + 1
                    q.append(next_n)
            # 데이크스트라 부분. 계속해서 갱신시켜줘야함.
            if visitied[next_n] > visitied[node] + 1:
                visitied[next_n] = visitied[node] + 1
            elif visitied[next_n] > visitied[node] and next_n == node*2:
                visitied[next_n] = visitied[node]

