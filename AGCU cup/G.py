n, k = map(int, input().split())
s = ""
for i in range(1, n+1):
    s += str(i)
print(int(s)%k)
#12345
#4
#1~10000000
#413926
