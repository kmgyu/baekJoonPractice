def shift_table(pt):
    m = len(pt)
    tbl = [m] * 26
    # alphabet shift table
    for i in range(m-1):
        tbl[ord(pt[i])-65] = m - 1 - i
    print(T)
    print(*tbl, sep="")
    return tbl

def search_horspool(T, P):
    print("horspool start")
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m-1
    while i <= n-1:
        k = 0
        print(f"current index : {i}")
        while k <= m-1 and P[m-1-k] == T[i-k]: # remember... it's reverse checking
            print(f'matching : {P[m-1-k]}, {T[i-k]}')
            k += 1
        if k == m:
            print(f"found at {i-m+1}")
            return i-m+1
        else:
            print(f"failed at text index: {i-k}, pattern index: {m-1-k}")
            tc = t[ord(T[i-k])-65]
            i += tc-k
            print(f"shifted {tc-k}")
    return -1

T = "I_LOVE_BANANA_YOU_LIKE_APPLE_AND_MANGO"
P = "APPLE"
result = search_horspool(T, P)
print(result)