k = int(input())
for i in range(k):
    t = int(input())
    d = [1, 2, 4]
    for i in range(3, t):
        d.append(d[i-1]+d[i-2]+d[i-3])
    print(d[t-1])