l, c = map(int, input().split())
alphabet = list(input().split())
alphabet.sort() #미리정렬해줌.
vowels = [False]*c #모음확인용.
for i in range(c):
    if alphabet[i] in ['a','e','i','o','u']:
        vowels[i] = True
visited = [False]*c #탐색용
temp = []
def dfs(start,cnt):
    if len(temp) == l and cnt > 0 and l - cnt > 1:
        print(*temp, sep="")
        return
    for i in range(start, c):
        if not visited[i]:
            temp.append(alphabet[i])
            visited[i] = True
            if vowels[i]: #모음확인 후 지워준다.
                cnt += 1
            dfs(i,cnt)
            if vowels[i]: #여기서 지워줌.
                cnt -= 1
            visited[i] = False
            temp.pop()

dfs(0,0)