
k = {'B':0, 'S':1, 'G':2, 'P':3, 'D':4}
input=open(0).readline
N=int(input())
P=input().split()
P_s=sorted(P, key=lambda x: (k[x[0]], -int(x[1:])))
w = []
for i in range(N):
    if P[i]!=P_s[i]:
        w.append(P[i])

if w:
    print('KO')
    print(*sorted(w, key=lambda x: (k[x[0]], int(x[1:]))))
else: print('OK')