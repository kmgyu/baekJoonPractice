import sys
def input() : return sys.stdin.readline().rstrip()

n, t = map(int, input().split())
tier = []
# actu = set()
m = n
for i in range(t):
    s, k = input().split()
    if k[-1] == "%":
        k = str(m*int(k[:-1]))[:-2]
        if k == '': k = 0
    k = int(k)
    k = min(m, k)
    tier.append((s, int(k)))
    # actu.add(s)
    m -= int(k)

friend = input()
if m > 0:
    print("Invalid System")
    exit()

ans = 0
idx = 0
ss = friend
if friend[-1] in ['1','2','3','4']:
    ss = friend[:-1]

# 티어별
# if ss not in actu:
#     print('liar')
#     exit()

for i in range(t):
    if tier[i][0] == ss:
        idx = i
        break
    ans += tier[i][1]

#세부분류
m = tier[idx][1]
k = []
detail = tier[idx][1]//4
if tier[idx][1]%4:
    detail+=1
for i in range(4):
    if m <= detail:
        k.append(m)
        break
    k.append(detail)
    m -= detail
if k[-1] == 0: k.pop()


if friend[-1] in ['1','2','3','4']:
    
    if len(k) < int(friend[-1]):
        print("Liar")
        exit()
    idx = 0
    for i in range(4):
        if i < int(friend[-1])-1:
            ans += k[i]
        else:
            idx = i
            break
    print(ans+1, ans+k[idx])
else:
    if not k:
        print("Liar")
    else:
        print(ans+1, ans+tier[idx][1])