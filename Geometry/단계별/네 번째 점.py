xcoor = []
ycoor = []
for i in range(3):
    a, b = map(int, input().split())
    if a in xcoor:
        xcoor.remove(a)
    else:
        xcoor.append(a)
    if b in ycoor:
        ycoor.remove(b)
    else:
        ycoor.append(b)
print(*xcoor, *ycoor)

