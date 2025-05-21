k = int(input())
x, y = map(int, input().split())
if 1 < x < k and 1 < y < k:
    print(4)
elif 1 < x < k or 1 < y < k:
    print(3)
elif x == y == k == 1:
    print(0)
elif x == 1 or y == 1 or x == k or y == k:
    print(2)