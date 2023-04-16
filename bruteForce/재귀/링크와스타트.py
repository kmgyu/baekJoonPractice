n = int(input())
stats = [list(map(int, input().split())) for i in range(n)]
visited = [0] * n
ans = 99999

def is_it():
    global ans
    start, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start += stats[i][j]
            elif not visited[i] and not visited[j]:
                link += stats[i][j]
    ans = min(ans, abs(start - link))
    return

def resolve(iter):
    if iter == n: #iter가 길이 넘기면 끝내고 함수호출
        is_it()
        return
    visited[iter] = 1
    resolve(iter + 1) #해당 pos에서 접근했을 때
    visited[iter] = 0
    resolve(iter + 1) #아닐때 2가지 경우
resolve(0)

print(ans)