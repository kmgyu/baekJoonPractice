from sys import stdin
input = stdin.readline

n,m = map(int,input().split())
a = list(map(int, input().split()))
for i in range(m-1):
    a[i+1] += a[i]

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start+1 < end:
        mid = (start+end) // 2
        if data[mid] <= target:
            start = mid
        else:
            end = mid
    if data[start] < target:
        if data[end] < target:
            return -1
        return end
    return start

for i in range(n):
    b = int(input())
    isT = False
    c = binary_search(b, a)
    if c != -1:
        print(c+1)
    else:
        print("Go away!")

