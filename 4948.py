input = open(0).readline

is_p = [1] * ((123456)*2+1)
is_p[1]=0
l = len(is_p)
for i in range(2, l//2):
    if is_p[i]:
        for step in range(i+i, l, i):
            is_p[step] = 0

while True:
    n = int(input())
    if n==0: break
    print(sum(is_p[n+1:2*n+1]))