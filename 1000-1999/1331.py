def atoi(s):
    # alphabet to integer. lol
    return ord(s) - ord('A') + 1

def parse(str):
    return atoi(str[0]), int(str[1])

def movement(prev, next):
    p, n = parse(prev), parse(next)
    n1 = abs(p[0]-n[0])
    n2 = abs(p[1]-n[1])
    n1, n2 = min(n1, n2), max(n1, n2)
    if (n1, n2) != (1, 2):
        return 0
    return 1

visited = []
L=36
first, last = '', ''
for i in range(L):
    s = input()
    visited.append(s)
    if i == 0: first = s
    if i == 35: last = s

for i in range(len(visited)-1):
    if not movement(visited[i], visited[i+1]):
        print("Invalid")
        exit()

if movement(first, last) and len(set(visited)) == L: print("Valid")
else: print("Invalid")