from sys import stdin
input = stdin.readline
ans = []
for i in range(int(input())):
    ans.append(list(input().split()))
ans = sorted(ans, key=lambda x:int(x[2]), reverse=True)
print(*ans[0][:2])
print(*ans[1][:2])
if ans[0][0] == ans[1][0]:
    for i in range(2, len(ans)):
        if ans[i][0] != ans[0][0]:
            print(*ans[i][:2])
            break
else:
    print(*ans[2][:2])