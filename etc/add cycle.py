#1110번
n = input().zfill(2)
temp = str(n)
count = 0
while True:
    a = str(sum(map(int, temp))).zfill(2)
    count += 1
    if temp[1] + a[1] == n:
        break
    temp = temp[1] + a[1]
print(count)

# 다른 사람꺼 돚거. 이 사람은 몫과 나머지를 이용했다.
# def main():
#     init_num = int(input())
#     cur_num = init_num
#     count = 0
#     while (True):
#         x = cur_num // 10
#         y = cur_num % 10
#         value1 = y
#         value2 = (x + y) % 10
#         cur_num = int(str(value1) + str(value2))
#         count += 1
#         if cur_num == init_num: break
#
#     print(count)