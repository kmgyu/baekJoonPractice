
#밀도 = 질량/부피
#질량 = c, 부피 = ?
#질량/부피 해서 밀도 구한후 더하면 됨.

# 8 = 50 / ?
# 50/8
#6.25
# 50/10
#5

a, b, c = map(int, input().split())
c = c
if a > b:
    a = c / a
    b = (100-c) / b
else:
    a = (100-c) / a
    b = c / b
print(100/(a+b))