import sys
input = sys.stdin.readline

def distance(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def strip_closest(P, d):
    n = len(P)
    d_min = d
    P.sort(key=lambda x: x[1])
    
    for i in range(n):
        j=i+1
        while j<n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j+=1
    return d_min

def closest_merge(P, n):
    d_min = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            d_min = min(d_min, distance(P[i], P[j]))
    return d_min

def closest_pair(P, n):
    if n<=3:
        return closest_merge(P, n)
    
    mid = n//2
    L = P[:mid]
    R = P[mid:]
    
    dL = closest_pair(L, mid)
    dR = closest_pair(R, n-mid)
    d = min(dL, dR)
    
    Pm=[]
    for i in range(n):
        if abs(P[i][0] - P[mid][0])**2 < d:
            Pm.append(P[i])
    ds = strip_closest(Pm, d)
    return ds

def data():
    n = int(input())
    P = [list(map(int, input().split())) for _ in range(n)]
    P.sort()
    return P, n

print(closest_pair(*data()))