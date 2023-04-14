n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(start, n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(i)
            visited[i] = False
            temp.pop()

dfs(0)