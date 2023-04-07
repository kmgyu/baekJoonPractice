#10807번 개수세기
count = int(input())
nums = input().split()
comp = int(input())
count_num = 0
for i in range(count):
    if int(nums[i]) == comp:
        count_num += 1
print(count_num)

"""
개쩌는 숏코딩
import sys 
N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
find = int(input())

count = 0
for i in range(len(lst)) :
    if lst[i] == find : count += 1
print(count)
"""