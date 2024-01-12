import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def find(n):
    if tree[n][1] == -1: return n
    else: return find(tree[n][1])

def dfs(num):
    global last, cnt
    if tree[num][0] != -1:
        dfs(tree[num][0])
        cnt += 1
    if num == last: print(cnt); exit(0)
    cnt += 1
    if tree[num][1] != -1:
        dfs(tree[num][1])
        cnt += 1
    
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n):
    a, b, c = map(int, input().split())
    tree[a]= (b,c)
cnt = 0
last = find(1)
dfs(1)