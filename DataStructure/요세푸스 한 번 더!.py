import sys
input = sys.stdin.readline
while True:
    s = input().rstrip()
    if s == '0':
        break
    n,a,b=map(int, s.split())
    graph = set()
    index = 0
    man = []
    while True:
        man.append(index)
        if index in graph :
            break
        graph.add(index)
        index = (a*(index**2)+b)%n
    print(n - (len(graph) - man.index(index)))
    # for i in range(0, n, (a*i+b)%n)