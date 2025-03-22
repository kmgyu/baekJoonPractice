def query(n, num):
    global cookie
    if n == 1:
        for i in range(4):
            if need[i] * num > got[i]:
                print("Hello, siumii")
                break
        else:
            for i in range(4):
                got[i] -= need[i]*num
            cookie += num
            print(cookie)
    
    else:
        got[n-2] += num
        print(got[n-2])

input = open(0).readline
got = [*map(int, input().split())]
need = [*map(int, input().split())]
cookie = 0
Q = int(input())

for i in range(Q):
    query(*map(int, input().split()))