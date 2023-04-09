from itertools import combinations


t = int(input())
for i in range(t):
    num = list(map(int,input().split()))
    li = list(combinations(num[1:], 2))
    gcd = []
    for i in li:
        a, b = i[0], i[1]
        num = a*b
        if a < b :
            a, b = b, a
        while b > 0:
            temp = a
            a = b
            b = temp%b
        #a == gcd
        gcd.append(a)
    print(sum(gcd))