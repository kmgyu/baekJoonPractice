a = set()
for i in range(5):
    s = int(input())
    if s in a: a.remove(s)
    else: a.add(s)
print(*a)