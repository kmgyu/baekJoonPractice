import sys
# https://peisea0830.tistory.com/103
input = sys.stdin.readline

n = int(input())

zero = set()
coor = []
for i in range(n):
    a, b = map(int, input().split())
    coor.append((a, b))
    
for i in range(n):
    x1, y1 = coor[i]
    x2, y2 = coor[(i+1) % n]
    if x1 == x2 and y1 * y2 < 0: zero.add(x1)
zero = sorted(zero)

cache = dict()
for i in range(len(zero)):
    cache[zero[i]] = i

res = []
now = []

check = [False] * n
temp = sorted(coor, key=lambda x : (x[0], x[1]))

val = temp[0]
idx = -1
for i in range(n):
    if coor[i] == val:
        idx = i
        break

while not check[(idx + 1) % n]:
    check[idx] = True
    x1, y1 = coor[idx]
    x2, y2 = coor[(idx + 1) % n]
    if x1 == x2 and y1 * y2 < 0:
        now.append(x1)
        if len(now) >= 2:
            first = now.pop()
            second = now.pop()
            res.append((min(first, second), max(first, second)))
    idx += 1
    idx %= n

dots = dict().fromkeys(zero)
for i in res:
    idx1 = cache[i[0]]
    idx2 = cache[i[1]]
    dots[i[0]] = (1, idx1)
    dots[i[1]] = (-1, idx2)

st = []

outside = 0
inside = 0

cnt = 0
for i in dots:
    if dots[i][0] == -1:
        _, idx = st.pop()
        cnt -= 1
        if cnt == 0:
            outside += 1
        if abs(dots[i][1] - idx) == 1:
            inside += 1
            
    else:
        st.append(dots[i])
        cnt += 1

print(outside, inside)