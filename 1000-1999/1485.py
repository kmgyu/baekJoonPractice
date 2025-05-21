for i in range(int(input())):
    graph = []
    for i in range(4):
        graph.append(list(map(int,input().split())))
    distance = set()
    for i in range(4):
        for j in range(i+1, 4):
            distance.add(abs((graph[j][0]-graph[i][0])**2+(graph[j][1]-graph[i][1])**2))
    if len(distance) == 2 and max(distance) == min(distance)*2:
        print(1)
    else:
        print(0)