n=int(input())
mount=list(map(int, input().split()))
m=mount[0] #max
ans=0
cnt=0
for i in range(1,n):
    if mount[i] <= m:cnt+=1
    else:
        m=mount[i]
        ans=max(ans,cnt)
        cnt=0
print(max(ans,cnt))