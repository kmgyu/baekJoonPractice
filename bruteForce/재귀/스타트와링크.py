N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
arr=[]
arr2=[_ for _ in range(N)]
ansArr=[]
def cal_(a,b):
    asum=0
    for i in a:
        for j in a:
            if i==j:
                continue
            asum+=graph[i][j]
    bsum=0
    for i in b:
        for j in b:
            if i==j:
                continue
            bsum+=graph[i][j]
    ansArr.append(abs(asum-bsum))
def dfs():
    if len(arr)==N//2:
        
        cal_(arr,list(set(arr2)-set(arr)))
        return
    
    for i in range(N):
        if len(arr)==0 or i >max(arr):
            arr.append(i)
            dfs()
            arr.pop()
dfs()

print(min(ansArr))




# N=int(input())
# graph=[list(map(int,input().split())) for _ in range(N)]
# check = [False] * N
# ans = 10e9
# def myDfs(cnt, pos):
#     global ans
#     if cnt == N//2:
#         #계산
#         temp = 0
#         for i in range(N):
#             for j in range(N):
#                 if i == j:
#                     continue
#                 if check[i] and check[j]:
#                     temp += graph[i][j]
#                 elif not check[i] and not check[j]:
#                     temp -= graph[i][j]
#         ans = min(ans, abs(temp))
#         return
#     for i in range(pos, N):
#         check[i] = True
#         myDfs(cnt+1, pos+1)
#         check[i] = False

# myDfs(0, 1)
# print(ans)