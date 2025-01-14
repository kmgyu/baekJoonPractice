c = [0, True, False, False]
for i in range(int(input())):
    x,y=map(int,input().split())
    c[x],c[y]=c[y],c[x]
for i in range(4):
    if c[i]:
        print(i)
