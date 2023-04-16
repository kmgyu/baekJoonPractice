temp = []
def dfs(start):
    if len(temp) == 6:
        print(*temp)
        return
    for i in range(start, k[0]+1):
        if not visited[i]:
            temp.append(k[i])
            visited[i] = True
            dfs(i)
            visited[i] = False
            temp.pop()
while True:
    k = list(map(int,input().split())) #[0]은 k, 나머지는 집합s
    visited = [False]*(k[0]+1)
    #마지막에는 0이 입력된다.
    if k[0] == 0:
        break
    dfs(1)
    print()