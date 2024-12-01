# 단어장 프로그램
# 새로운 단어, 그 단어 의미 추가하는 삽입
# 단어 빨리 찾기
# 완전히 외운 단어 삭제
# 해시를 이용해 구현
# 오버플로 처리로는 체이닝. 해시맵으로 단어장 구현.


M = 1000
word_list = [[]] * M

def hash(word):
    global M
    return sum([ord(c) for c in word]) % M

def insert(word, meaning):
    id = hash(word) % 1000
    # chaining implemented by list lol
    if word_list[id]:
        print("conflict detected")
    word_list[id].append([word, meaning])

def search(word):
    id = hash(word) % 1000
    if word_list[id]:
        for w, m in word_list[id]:
            if w == word:
                print(f"word found: {w}, meaning: {m}")
                return w, m
    print(f"word not found {word}")
    return None

def delete(word):
    id = hash(word) % 1000
    if word_list[id]:
        for w, m in word_list[id]:
            if w == word:
                print(f"word found: {w}, meaning: {m}, deleted")
                word_list[id].remove([w, m])
                return w, m
    print(f"word not found {word}")
    return None

if __name__ == "__main__":
    while True:
        print("simple test driver. 1: insert, 2: search, 3: delete, 4: exit")
        cmd = int(input())
        if cmd == 1:
            word = input("word: ")
            meaning = input("meaning: ")
            insert(word, meaning)
        elif cmd == 2:
            word = input("word: ")
            search(word)
        elif cmd == 3:
            word = input("word: ")
            delete(word)
        elif cmd == 4:
            break
        else:
            print("invalid command")
            continue