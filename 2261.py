import sys
input = sys.stdin.readline

def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def closest_pair(start, end):
    if (end-start) <= 3: # brute force
        md = float('inf')
        for i in range(start, end-1):
            for j in range(i+1, end):
                md = min(md, dist(P[i], P[j]))
        return md
    
    mid = (start+end)//2
    
    dl = closest_pair(start, mid) # left d
    dr = closest_pair(mid, end) # right d
    d = min(dl, dr) # min dist
    
    Pm = [] # Pair minor than d
    mid_x = P[mid][0]
    for i in range(start, end):
        if (P[i][0] - mid_x)**2 < d:
            Pm.append(P[i])
    Pm.sort(key=lambda x: x[1])
    
    Pmn = len(Pm)
    for i in range(Pmn):
        now = Pm[i]
        for j in range(i+1, Pmn):
            compare = Pm[j]
            if (compare[1] - now[1])**2 > d: break
            d = min(d, dist(now, compare))
    return d

n = int(input())
P = [list(map(int, input().split())) for _ in range(n)]
P.sort()

print(closest_pair(0, n))