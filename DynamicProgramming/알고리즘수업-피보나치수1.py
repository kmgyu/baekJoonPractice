#24416번
n = int(input())
d = [1, 1]
for i in range(2, n):
    d.append(d[i-2]+d[i-1])
print(d[n-1])
print(n-2) #dp