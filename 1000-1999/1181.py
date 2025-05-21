#1181번
n = int(input()) #단어의 개수
word = []
for i in range(n):
    word.append(input())
word = list(set(word))
word.sort()
word.sort(key=len)

print(*word, sep="\n", end="")