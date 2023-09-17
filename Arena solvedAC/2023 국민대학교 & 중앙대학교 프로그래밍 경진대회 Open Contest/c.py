
s = ['F', 'D', 'C', 'B', 'A']

n, x = input().split()
n = int(n)
x = float(x)
score = []
hak = []
for i in range(n-1):
    c, g = input().split()
    c=int(c)
    ss = s.index(g[0])
    if g[1] == '+':
        ss += 0.5
    ss*=c
    score.append(ss)
    hak.append(c)

l = int(input())
hak.append(l)
if sum(score)/sum(hak) > x:
    print("F")
    exit()

tmp = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0']
for i in tmp[::-1]:
    ss = s.index(i[0])
    if i[1] == '+':
        ss += 0.5
    
    sscore = ss*l + sum(score)
    sscore /= sum(hak)
    sscore = int(sscore*100)/100
    if sscore > x:
        print(i)
        exit()

print("impossible")