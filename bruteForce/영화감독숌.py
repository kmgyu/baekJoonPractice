#1436
n = int(input())
m = 666
count = 1
while count < n:
    m += 1
    if '666' in str(m) :
        count += 1
print(m)

# 돚거한거. 미친듯.
# import sys

# N = int(sys.stdin.readline())

# count = 0

# def some_func(ord, padding, rept):
#     global count 
#     for i in range(rept):
#         count += 1
#         if count == N:
#             sys.stdout.write(str(ord * 1000 + padding + i))
#             exit()

# for i in range(N):
#     if i % 1000 == 666:
#         some_func(i, 0, 1000)
#     elif i % 100 == 66:
#         some_func(i, 600, 100)
#     elif i % 10 == 6:
#         some_func(i, 660, 10)
#     else:
#         some_func(i, 666, 1)