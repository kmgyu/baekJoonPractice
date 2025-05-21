n, m = map(int, input().split())
mission = list()
cnt = 0
for i in range(2):
    mission.append(list(map(int, input().split())))

def dfs(day, contribution, yester):
    global cnt
    if day == n:
        if contribution >= m:
            cnt+=1
        return
    for i in range(2):
        for j in range(3):
            temp = mission[i][j]
            if yester == j:
                temp //=2
            dfs(day+1, contribution+temp, j)

dfs(0, 0, 3)
print(cnt)