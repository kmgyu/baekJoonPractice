import sys
input = sys.stdin.readline

def dfs(num):
    global n # length of list
    tree[num] = -2
    for i in range(n):
        if num == tree[i]:
            dfs(i)

n = int(input())
tree = list(map(int, input().split()))

k = int(input())
cnt = 0
dfs(k)

branch = set(tree) # not a leaf
cnt = 0
for i in range(n):
    if tree[i] != -2 and i not in branch: cnt += 1
print(cnt)