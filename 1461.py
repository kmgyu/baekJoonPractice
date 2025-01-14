import sys
input = sys.stdin.readline
n, m = map(int, input().split())
book = list(map(int, input().split()))
book.sort()
b = book[:]
d = 0
while book and book[-1] > 0:
    cd = book[-1]
    for i in range(m):
        if not book or book[-1] <=0:break
        book.pop()
    d += cd * 2
book = book[::-1]
while book:
    cd = book[-1]
    for i in range(m):
        if not book: break
        book.pop()
    d -= cd * 2
print(d - max(-b[0],b[-1]))
