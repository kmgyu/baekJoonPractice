#10809번

s = input()
find = list()
for i in range(97, 123):
    find.append(s.find(chr(i)))
print(*find)