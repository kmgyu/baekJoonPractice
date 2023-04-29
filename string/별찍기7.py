n = int(input())
li = [" "*(n-i) + "*"*(i*2-1) for i in range(1,n+1)]
for a in li:
    print(a)
for b in range(n-2, -1, -1):
    print(li[b])