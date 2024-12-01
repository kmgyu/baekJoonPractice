# reference: https://www.geeksforgeeks.org/boyer-moore-algorithm-good-suffix-heuristic/
# jesus christ

def shift_table(pt): # bad-symbol rule. equal to horspool algorithm's shift table
    m = len(pt)
    pt_set = set(pt)
    tbl = {i:m for i in pt_set} # optimized shift table
    for i in range(m-1):
        tbl[pt[i]] = m - 1 - i
    # print(tbl) # check shift table
    return tbl

def good_suffix(P): # good suffix rule
    m = len(P) # length of pattern
    shift = [0] * (m+1) # shift table
    bpos = [0] * (m+1) # border position (what the hell is this)
    
    i, j = m, m+1
    bpos[i] = j
    # case 1, suffix is in pattern (except prefix)
    while i>0:
        # print("blahblah")
        # print(i, P[i:], j, P[j:])
        # print(shift, bpos)
        while j <= m and P[i-1] != P[j-1]: # find border position (end point? i guess...)
            # it's similar with shift table. no nevermind i don't get it
            if shift[j] == 0: # 0 == none
                shift[j] = j-1 # save shift value
            j = bpos[j] # to the next border position. for make it faster
            # print(i, P[i:], j, P[j:])
            # print(shift, bpos)
            # so... if not found a matched char, j will be not discounted. jesus what the hell is this so complicated and unfriendly
        i-=1 # discount both.
        j-=1
        bpos[i] = j # save the last point of border position
        # additionally, i == 0, uhh.... idk. what the
    # print("case 1 end")
    
    # case 2, prefix == suffix
    j = bpos[0]
    for i in range(m+1):
        # print(i, P[i:], j, P[j:])
        # print(shift, bpos)
        if shift[i] == 0: # we already searched except prefix. so we can skip the sub-patterns thas is not 'pre'.
            shift[i] = j # yessss it's saving the shift value
        if i == j: # what the...
            j = bpos[j] # yes.. it's saving the border position
    return shift


def solve(T, P): #boyer-moore algorithm
    m = len(P)
    n = len(T)
    bad_symbol = shift_table(P)
    good_suffix_table = good_suffix(P)
    
    s = 0
    while s <= n-m:
        j = m-1
        while j>=0 and P[j] == T[s+j]:
            j-=1
        
        if j<0:
            print(f"pattern found at {s}") # return quickly
            # s += good_suffix_table[0]
            return s
        else:
            print(f"shift from pattern {s}")
            bad = m
            if T[s+j] in bad_symbol:
                bad = j-bad_symbol[T[s+j]]
                
            if j == 0: s += bad # bad symbol rule...
            else: s += good_suffix_table[j+1] # good suffix rule. is this a.... well. my brain has melted already

T="I_LOVE_BANANA_YOU_LIKE_APPLE_AND_MANGO"
P="BANANA"
solve(T, P)