#2108번
import sys
N = int(sys.stdin.readline())
num = [0] * 8001
num_set = set()
for i in range(N):
    a = int(sys.stdin.readline())
    num[a+4000] += 1
    num_set.add(a)

num_sum = 0
for i in range(len(num)):
    num_sum += (i-4000)*num[i]
if num_sum >= 0:
    print(int(num_sum/N+0.5))
else:
    print(int(num_sum / N - 0.5))

num_set = sorted(list(num_set))
m = max(num)
num_middle = list()
for i, v in enumerate(num):
    num_middle += [i-4000] * v
print(num_middle[int(N/2)])
num_max = [i-4000 for i, v in enumerate(num) if v == m]
if len(num_max) > 1:
    print(num_max[1])
else:
    print(num_max[0])
print(num_set[len(num_set)-1] - num_set[0])

# collections 라는 모듈을 썼다. 꼭 찾아보시오....
# import sys
# import collections
# n = int(sys.stdin.readline())
#
# ans = []
# for _ in range(n):
#     ans.append(int(sys.stdin.readline()))
# ans.sort()
#
# print(round(sum(ans)/n))
# print(ans[n//2])
#
# if n==1:
#     print(ans[0])
# else:
#     most_common = collections.Counter(ans).most_common() # [값, 갯수]로 반환
#     if most_common[0][1] == most_common[1][1]:
#         print(most_common[1][0])
#     else:
#         print(most_common[0][0])
# print(ans[-1]-ans[0])