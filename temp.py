d = ['W', 'N', 'E', 'S']
dd = 1
for i in range(10):
    t  = int(input())
    if t == 1:
        dd += 1
    if t == 2:
        dd += 2
    if t == 3:
        dd -= 1
print(d[dd%4])