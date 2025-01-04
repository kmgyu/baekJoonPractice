n = int(input())
p = ["bowling", "soccer"]
for i in range(1500):
    print("swimming", end=" ")
print()
a = list(input().split())
for i in a:
    if i == p[0]:
        print(p[1], end=" ")
    else:print(p[0], end=" ")