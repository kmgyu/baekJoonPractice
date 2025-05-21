s = []
for i in range(int(input())):
    a = int(input())
    if a:
        s.append(a)
    else:
        s.pop()
print(sum(s))