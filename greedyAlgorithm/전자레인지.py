b=[300,60,10]
t=int(input())
ans=[]
for i in b:ans.append(t//i);t%=i
if t:print(-1)
else:print(*ans)