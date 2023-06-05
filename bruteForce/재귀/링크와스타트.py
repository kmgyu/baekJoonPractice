import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited1 = [False] * n
min_value = 100*20

def recur(target):
    if target == n:
        score()
        return
    visited1[target] = True
    recur(target+1)
    visited1[target] = False
    recur(target+1)

def score():
    global min_value
    start = 0
    link = 0

    for i in range(n-1):
        for j in range(i+1,n):
            if visited1[i] and visited1[j] :
                start += matrix[i][j] + matrix[j][i]
            elif not visited1[i] and not visited1[j]:
                link += matrix[i][j] + matrix[j][i]
    diff = abs(start-link)
    if  min_value > diff:
        min_value = diff

recur(0)
print(min_value)
# https://velog.io/@gandi0330/Python-%EB%B0%B1%EC%A4%80-%EB%A7%81%ED%81%AC%EC%99%80-%EC%8A%A4%ED%83%80%ED%8A%B8-15661%EB%B2%88-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4