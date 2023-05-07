from sys import stdin
input = stdin.readline
m=['a','e','i','o','u']
while True:
    s = input().rstrip().lower()
    if s == "#": exit()
    cnt = 0
    for i in s:
        if i in m: cnt += 1
    print(cnt)