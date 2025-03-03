from itertools import combinations

input = open(0).readline
def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))
    return bit

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))
base_bit = word2bit('antic') # 초깃값. 이건 꼭 포함됨.

if K < 5:
    print(0)
else:
    # base bit이랑 안겹치는 걸 조합에 넣어줘야함.
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
    answer = 0
    for combination in combinations(alphabet, K-5): # 기본 비트 antic 제외
        know_bit = sum(combination) | base_bit
        count = 0
        for bit in bits:
            if bit & know_bit == bit:
                count += 1
        answer = max(answer, count)
    print(answer)
