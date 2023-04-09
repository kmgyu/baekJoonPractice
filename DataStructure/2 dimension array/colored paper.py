loop = int(input())
location = list()
paper = [[False]*100 for i in range(100)] #중요! [[False] * 100] * 100의 경우 얕은 복사때문에 배열이 개판이 된다.
count = 0
for i in range(loop):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            paper[j][k] = True

for i in range(100):
    for j in range(100):
        if paper[i][j]:
            count += 1

print(count)