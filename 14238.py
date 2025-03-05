# solve with greedy, reference : https://oculis.tistory.com/55
# dp인척하는 그리디 XD
# dp로 풀 수도 있고, 그리디로 풀 수도 있다. 답은 여러개~
s=input()
cnt = [0,0,0]
for i in s:
    if i == 'A': cnt[0]+=1
    elif i == 'B': cnt[1]+=1
    else: cnt[2]+=1

ans = '  '
n = sum(cnt)

for i in range(2, n+2):
    if not (ans[-1]!='B' and cnt[1]>(n+2-i)//2) and (cnt[2]>0 and 'C' not in ans[-2:]):
        ans += 'C'
        cnt[2] -= 1
    elif ans[-1] != 'B' and cnt[1] > 0:
        ans += 'B'
        cnt[1] -= 1
    elif cnt[0] > 0:
        ans += 'A'
        cnt[0] -= 1
if len(ans) == n+2: print(ans[2:])
else: print(-1)
