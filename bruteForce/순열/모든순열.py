n = int(input())
nums = list(range(1, n+1))
temp = []
visited = [False]*n

def dfs():
    if len(temp) == n:
        print(*temp)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp.append(nums[i])
            dfs()
            visited[i] = False
            temp.pop()

dfs()

