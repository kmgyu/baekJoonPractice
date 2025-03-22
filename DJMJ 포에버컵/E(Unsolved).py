# bit masking을 이용한.... 으에...
# 부분집합 계산하기 인데... 일반적인 연산으로는 어려운 것으로 보임.
# Subset Problem을 응용해야 하나? 그런 문제는 아닌거같은데
# 세그먼트 트리도 아닌듯. 트라이?도 아닐텐데

def insert(K, i, genres, current):
    # dfs bit mapping
    bit = bit_mapper(current)
    if bit not in search: search[bit] = 0
    search[bit] += 1
    
    if i == K: return
    for idx in range(i, K):
        insert(K, idx+1, genres, current+[genres[idx]])
    

def bit_mapper(genres):
    bits = 0
    for genre in genres:
        bits |= tags[genre]
    return bits
    # return bin(bits) # 문자열은 속도가 영향이 없나보이


input = open(0).readline

N = int(input())
genre = input().split()

tags = dict()
for i in range(N): # bit로 저장
    tags[genre[i]] = 1 << i

search = dict()

M = int(input())
for i in range(M):
    book = input().split()
    insert(int(book[0]), 0, book[2:], [])

Q = int(input())
for i in range(Q):
    question = input().split()
    bit = bit_mapper(question[1:])
    if bit in search: print(search[bit])
    else: print(0)

# print(tags)
# print(search)