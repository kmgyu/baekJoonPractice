#2566번
matrix = list()
temp = list()
a = list()
for i in range(9):
    matrix.append(list(map(int,input().split())))
    a.append((matrix[i].index(max(matrix[i]))))
    temp.append(matrix[i][a[i]])

print(max(temp))
print(temp.index(max(temp))+1, a[temp.index(max(temp))]+1)

