def shift_table(pt):
    m = len(pt)
    texts = "ACGT"
    tbl = {texts[i]:m for i in range(4)}
    # A, C, G, T shift table
    for i in range(m-1):
        tbl[pt[i]] = m - 1 - i
    # print(texts)
    print(tbl)
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
        print(f"{T[0:i-m+1]} {T[i-m+1:i+1]} {T[i+1:]}")
        while k <= m-1 and P[m-1-k] == T[i-k]: # remember... it's reverse checking
            print(f'matching : {P[m-1-k]}, {T[i-k]}')
            k += 1
        if k == m:
            print(f"found at {i-m+1}")
            return i-m+1
        else:
            print(f"failed at text index: {i-k}, pattern index: {m-1-k}")
            tc = t[T[i-k]]
            i += tc-k
            print(f"shifted {tc-k}")
    return -1

T = "TTATAGATCTCGTATTCTTTTATAGATCTCCTATTCTT"
P = "TCCTATTCTT"
start_index = search_horspool(T, P)
print(T[start_index : start_index+len(P)])