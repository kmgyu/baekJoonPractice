
x=int(input())

d=[[0, 0] for _ in range(x+1)]
d[1][1] = 1
for i in range(2,x+1):
    d[i][0]=d[i-1][0]+1
    d[i][1] = i-1
    if i%2==0:
        if d[i][0] > d[i//2][0]:
            d[i][0] = d[i//2][0]+1
            d[i][1] = i//2
    if i%3==0:
        if d[i][0] > d[i//3][0]:
            d[i][0] = d[i//3][0]+1
            d[i][1] = i//3
print(d[x][0])
i = x
# print(d)
while i != 1:
    print(i, end=" ")
    i = d[i][1]
print(1)