n = int(input())
name = [input() for _ in range(n)]
cnt = 0
for i in range(n):
    ilen = len(name[i])
    for j in range(i+1, n):
        jlen = len(name[j])
        for k in range(min(ilen, jlen)+1):
            if name[i][:k] == name[j][-k:] or name[i][-k:] == name[j][:k]:
                cnt += 1
                break
print(cnt)