n = int(input())
div = set(input().split())
m = int(input())
div = div.union(input().split())
k = int(input())
merge = set(input().split())

length = int(input())
s = list(input())

div = div.difference(merge)

for i in range(length):
    if s[i] in div or s[i] == ' ':
        s[i] = '\n'

s = ''.join(s).split()
print(*s, sep="\n")
