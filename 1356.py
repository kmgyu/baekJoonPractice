N = input()

def parslice(start, end):
    # parse and slice
    s = 1
    for i in range(start, end):
        s *= int(N[i])
    return s

l = len(N)
for i in range(l-1):
    a = parslice(0, i+1)
    b = parslice(i+1, l)
    if a == b:
        print('YES')
        break
else:
    print('NO')