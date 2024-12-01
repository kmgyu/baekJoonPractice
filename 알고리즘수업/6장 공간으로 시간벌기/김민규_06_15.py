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

T = "ACGT"
P = "TCCTATTCTT"

shift_table(P)