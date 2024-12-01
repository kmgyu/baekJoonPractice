

def shift_table(pt):
    m = len(pt)
    tbl = [m] * 26
    # alphabet shift table
    for i in range(m-1):
        tbl[ord(pt[i])-65] = m - 1 - i
    print(T)
    print(*tbl, sep="")
    return tbl

T = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
P = "APPLE"

shift_table(P)