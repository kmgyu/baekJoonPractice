n = int(input())
word = []
alpha = dict()
trans = dict()
for i in range(n):
    w = input().rstrip()
    word.append(w)
    for w1 in w:
        alpha[w1] = 0

for i in range(n):
    length = len(word[i])
    for j in range(length):
        alpha[word[i][j]] += 10**(length-j)

res = [(k,v) for k,v in alpha.items()]
res.sort(key = lambda x: -x[1])
for i in range(len(res)):
    a, b = res[i]
    trans[a] = 9-i

ans = 0
for i in range(n):
    s = ""
    for w in word[i]:
        s += str(trans[w])
    ans += int(s)
print(ans)