import sys
N = int(sys.stdin.readline())
count = [0] * 10001

for i in range(1, N+1):
    count[int(sys.stdin.readline())] += 1

for i in range(1, len(count)):
    for j in range(count[i]):
        print(i)


#메모리 제한!!!! 왤케!!! 옹졸하냐고!!!!!!
#어쨌든 카운팅정렬임. O(N)의 시간복잡도를 가진다. 정해진 숫자안에서의 카운팅정렬...

# import sys
#
# input = sys.stdin.readline
# print = sys.stdout.write
#
# def main():
#     N = int(input())
#
#     arr = [0] * 10001  # idx 가 0 부터 10000 까지
#
#     for _ in range(N):
#         arr[int(input())] += 1
#
#     for i in range(len(arr)):
#         if arr[i]:
#             while arr[i] > 1000:
#                 print((str(i) + '\n') * 1000)
#                 arr[i] -= 1000
#             print((str(i) + '\n') * arr[i])
#
# if __name__=="__main__" :
#     main()