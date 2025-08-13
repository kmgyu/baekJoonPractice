
# dp를 이용해서 구한다.
# 길이만 출력하는 방법.
def longest_common_substring1(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # DP 테이블
    max_length = 0  # 최장 공통 부분 문자열 길이

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:  # 문자가 같으면
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0  # 문자가 다르면 초기화

    return max_length

# dp에서 문자열을 복원하는 방법이다.
def longest_common_substring2(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index_a = 0  # A에서 공통 부분 문자열의 끝 위치

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:  # 문자가 같으면
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index_a = i  # A에서의 끝 위치
            else:
                dp[i][j] = 0

    # 공통 부분 문자열 복원
    start_index_a = end_index_a - max_length
    lcs = a[start_index_a:end_index_a]

    return max_length, lcs

# 메모리 최적화
def longest_common_substring(a, b):
    m, n = len(a), len(b)
    prev = [0] * (n + 1)
    max_length = 0
    end_index_a = 0

    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1] + 1
                if curr[j] > max_length:
                    max_length = curr[j]
                    end_index_a = i
            else:
                curr[j] = 0
        prev = curr

    # 공통 부분 문자열 복원
    start_index_a = end_index_a - max_length
    lcs = a[start_index_a:end_index_a]

    return max_length, lcs