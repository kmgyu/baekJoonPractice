import sys

input = sys.stdin.readline
print = sys.stdout.write
t = int(input())
for i in range(t):
    k = input().split()
    k = list(map(list, k))
    for j in range(len(k)):
        k[j].reverse()
        print(''.join(k[j]))
        if j < len(k)-1:
            print(" ")
    print("\n")

# reverse 내장함수를 안쓰고 최대한 간결하게 만듬.
# import sys
# N = int(input())
#
# for _ in range(N):
#     str = sys.stdin.readline().rstrip()
#     words = list(str.split())
#     reverse_words = []
#
#     for word in words:    word(단어)를 하나하나 역순으로 만들어서 reverse_words에 넣음.
#         reverse_words.append(word[::-1])
#
#     answer = " ".join(reverse_words)
#     print(answer)