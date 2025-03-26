N, M = map(int, input().split())

row = set()
col = set()

for i in range(N):
    s = input()
    for j in range(M):
        if s[j] == 'X':
            row.add(i)
            col.add(j)

row_m, col_m = set(range(N)), set(range(M))

k = max(len(row_m.difference(row)), len(col_m.difference(col)))
print(k)