# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 1181번
    n = int(input())  # 단어의 개수
    word = list()
    for i in range(n):
        word.append(input())  # 단어 추가

    # for문, n번 반복
    # 문자열 먼저 검사
    # 비교문 while 넣을거 > 뒤에거 이 이후 같을 시 작을 시 if문
    # 문자열이 같을 시 sort()하고 붙이기?
    ans = []
    for i in range(n):
        j = 0
        while (word[i] > ans[j]) and ans:
            j += 1
    ans.insert(j, word[i])

print(*ans, sep="\n")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
