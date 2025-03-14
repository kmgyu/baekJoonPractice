# 1014와 달리, 비트마스킹을 할 수 없다. 2^80이 되서 Overflow가 되기 때문.
# 따라서 이분매칭만을 이용해야 한다.
# 기존 왼쪽/오른쪽 위 중간에 더해 뒤쪽에 존재해도 그 학생이 컨닝할 수 있기 때문에, 범위를 확장한다.
# 그래서 홀/짝 열 두그룹으로 분리한다.
# 굉장히... 으에... 에///?? 문제.. 몬가ㅣ.... 으에...
# https://restudycafe.tistory.com/470

# https://velog.io/@gmtmoney2357/%EC%9D%B4%EB%B6%84-%EB%A7%A4%EC%B9%ADBipartite-Matching
# 이분매칭 레퍼런스 추가.

input = open(0).readline



dir = [
    [1, 1],
    [0, 1],
    [-1, 1],
    [1, -1],
    [0, -1],
    [-1, -1]
]



def solve():
    
    def dfs(x):
        # print(x)
        # x : current, y : next
        visited[x] = True
        for i in range(len(adj[x])):
            y = adj[x][i]
            if right[y] == -1 or (not visited[right[y]] and dfs(right[y])):
                left[x], right[y] = y, x
                return True
        return False
    
    N, M = map(int, input().split())
    room = ['x'*M]+[input() for _ in range(N)]
    cnt = sum([room[i].count('.') for i in range(N)])
    
    LENGTH = (80**2)+5
    
    adj = [[] for _ in range(LENGTH)]
    left = [-1]*LENGTH
    right = [-1]*LENGTH
    visited = []
    
    for i in range(1, N+1):
        for j in range(1, M+1):
            for k in range(6):
                if room[i][j] == 'x': continue
                cx = i + dir[k][0]
                cy = j + dir[k][1]
                if 1 <= cx < N and 1 <= cy < M and room[cx][cy] == '.':
                    adj[(i-1)*80 + j].append((cx-1)*80 + cy)
    
    match = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            visited = [False]*LENGTH
            if dfs( (i-1)*80+j ): match += 1
    print(cnt - match)
    

T = int(input())
for i in range(T):
    solve()