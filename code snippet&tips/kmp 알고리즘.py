# gpt와 함께하는 신나는 kmp 알고리즘

# lps : Longest Proper Prefix which is also Suffix
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0  # 길이를 나타내는 포인터 변수이름 꼬라지

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    result = []
    j = 0  # 패턴 포인터

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            result.append(i - m + 1)  # 패턴의 시작 인덱스 저장
            j = lps[j - 1]

    return result

# 예제 실행
text = "ababcababcabc"
pattern = "ababc"
matches = kmp_search(text, pattern)
print("패턴이 발견된 위치:", matches)
