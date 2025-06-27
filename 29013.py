a, b, c, d, k = map(int, input().split())

l,r = b,d
if l+r < k:
    print(-1)
else:
    while True:
        cur = l+r
        mod = cur%k
        if mod:
            if r-c + l-a < mod:
                print(-1); break
            if r-c >= mod:
                r -= mod
                mod = 0
            else: mod -= r-c; r = c
            
            if l-a >= mod:
                l -= mod
                mod = 0
            else: mod = l-a; l = a
        else:
            print(l, r)
            break