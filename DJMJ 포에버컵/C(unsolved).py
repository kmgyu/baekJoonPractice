def query(current):
    t = []
    for num in current:
        if num > 4 and sum(map(int, str(num-1) )) % 3 == 0:
            t.append((num-1) // 3)
        t.append(num*2)
    return t

N = int(input())

l = [1]

for i in range(N-1):
    l=query(l)
    print(len(l), end=' ')
print()
print(*sorted(set(l)), sep="\n")
