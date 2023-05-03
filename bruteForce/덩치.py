from sys import stdin
input = stdin.readline
n = int(input())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
ans = [0]*n

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j :
            continue
        if (table[i][0] >= table[j][0] and table[i][1] < table[j][1]) or (table[i][0] < table[j][0] and table[i][1] >= table[j][1]):
            continue
        if table[i][0] < table[j][0] or table[i][1] < table[j][1]:
            rank += 1
    ans[i] = rank
print(*ans)