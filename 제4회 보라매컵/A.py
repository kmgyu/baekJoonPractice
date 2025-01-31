N, M = map(int, input().split())

# m = M*100//N # 몫
m = M*10000//N # 몫
# n = (M*10000//N)%100 # 나머지

whole = m * 24

hour = whole // 10000
minute = (whole - hour * 10000) * 60 // 10000
# print(m)
# print(m*24//100)
# print()
# print(m, n)
print(f'{str(hour).zfill(2)}:{str(minute).zfill(2)}')
