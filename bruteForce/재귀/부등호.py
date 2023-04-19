# 처음으로 자력으로 푼 dfs 문제(백트래킹)

nums = list(range(10))
k = int(input())
sign = list(input().split())
visited = [False] * 10
temp = []
low = 10000000000
upp = -1

def dfs(cnt): #cnt 다찰경우 출력
    global low, upp
    if cnt == k+1:
        low = min(int("".join(list(map(str, temp)))),low) #012456
        upp = max(int("".join(list(map(str, temp)))),upp)
        #앞에 0이올경우 잘림. 이거 마지막에 수정하면 될듯.
        return
    for i in range(10):
        if visited[i]:
            continue
        if temp and cnt>0:
            if temp[-1] < i and sign[cnt-1] == ">":
                continue
            elif temp[-1] > i and sign[cnt-1] == "<":
                continue
        
        
        visited[i] = True
        temp.append(i)
        dfs(cnt + 1)
        temp.pop()
        visited[i] = False
    return
    #방문 시 False리턴
    #visited 스킵
    #성립안될경우 종료
dfs(0)

if len(str(low)) < k+1:
    low = "0" + str(low)
if len(str(upp)) < k+1:
    low = "0" + str(upp)
print(upp)
print(low)