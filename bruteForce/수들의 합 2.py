import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=[int(x) for x in input().split()]
end=0
sums=0
cnt=0
for start in range(n):
    while sums<m and end<n:
        sums+=num[end]
        end+=1
    if sums==m:
        cnt+=1
    sums-=num[start]
print(cnt)
#돚거한거임. 잘만들었어...
#start를 n번 조사하는데, sums에 넣고 계속 조사한다.
#만약 m을 찾으면 끝내고 cnt+1
#start에선 더 조사할수 없으므로 버린다.
