n = int(input())
coor = [list(map(int, input().split())) for _ in range(n)]
distance = [((coor[i][0]-coor[i-1][0])**2 + (coor[i][1]-coor[i-1][1])**2)**0.5 for i in range(n)]
print(int(sum(distance)))