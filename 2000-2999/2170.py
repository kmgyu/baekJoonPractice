from sys import stdin
#https://blog.naver.com/PostView.naver?blogId=kks227&logNo=220907708368&redirect=Dlog&widgetTypeCall=true&directAccess=false
#스위핑 알고리즘의 가장 기초적인 문제이다.
#근데 기초적인게 골드라고....?
input = stdin.readline
n = int(input())
line = []
for i in range(n):
    line.append(list(map(int,input().split())))
line.sort()
ans = 0
l, r = 0, 0
for i in range(n):
    if i == 0:
        l = line[i][0]
        r = line[i][1]
    if r >= line[i][0] >= l and r <= line[i][1]:
        r = line[i][1]
    elif r < line[i][0]:
        ans += r-l
        l = line[i][0]
        r = line[i][1]
ans += r-l
print(ans)