import sys
input = sys.stdin.readline

def find(n):
    if n != city[n]:
        city[n] = find(city[n])
        return city[n]
    return n


def union(a, b):
    parent = find(a) 
    child = find(b)
    if parent>child: parent, child = child, parent
    if parent != child: 
        city[child] = parent

n = int(input())
m = int(input())

city = list(range(n+1))

for i in range(1, n+1):
    edge = [0]+list(map(int, input().split()))
    for j in range(1, n+1):
        if edge[j]:
            union(i, j)

trip = list(map(int, input().split()))
# print(city)
tmp = city[trip[0]]
for i in range(1, m):
    if tmp != city[trip[i]]:
        print("NO")
        exit()
print("YES")