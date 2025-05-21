from itertools import permutations
n, k = map(int, input().split())
candy = [chr(i) for i in range(65, 65+n)]
li = list(permutations(candy, r=k))
limit = len(li)
visit = [False] * limit

def dfs():
    if len(stack) == limit:
        if stack[0][:-1] != stack[-1][1:]: return
        print("YES")
        for i in stack:
            print(*i, sep="", end=" ")
        exit()
    for i in range(limit):
        if visit[i]: continue
        if stack[-1][1:] == li[i][:-1]:
            visit[i] = True
            stack.append(li[i])
            dfs()
            visit[i] = False
            stack.pop()

for i in range(limit):
    stack = [li[i]]
    visit[i] = True
    dfs()
    visit[i] = False
print("NO")