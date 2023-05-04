coor = []
for i in range(3):
    coor.append(list(map(int, input().split())))
g = []
for i in range(3):
    for j in range(i+1,3):
        g.append([(coor[i][1]-coor[j][1]),(coor[i][0]-coor[j][0])])
cnt = 0
for i in range(len(g)):
    for j in range(i+1,len(g)):
        if g[i][0] * g[j][1] == g[i][1] * g[j][0]:
            cnt += 1
if cnt == 3:
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')