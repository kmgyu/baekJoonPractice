finder = set(['M','O','B','I','S'])
a = set()
s = input()
for i in s:
    if i in finder:
        a.add(i)

if a == finder:
    print("YES")
else:
    print("NO")