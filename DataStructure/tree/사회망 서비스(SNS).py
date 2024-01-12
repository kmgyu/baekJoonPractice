import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    if not edge[start]: # len(edge[start]) == 0
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in edge[start]:
            if not visited[i]:
                dfs(i)
                dp[start][1] += min(dp[i][0] , dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

n = int(input())
edge = [[] for _ in range(n)]
dp = [[0,0] for _ in range(n)]

for _ in range(n-1):
    a,b = map(int, input().split())
    a-=1;b-=1
    edge[a].append(b)
    edge[b].append(a)

visited = [False for _ in range(n)]

dfs(0)
print(min(dp[0][0],dp[0][1]))