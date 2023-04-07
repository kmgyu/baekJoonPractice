#10808번 알팓ㄷ벳 개수
s = input()
alphabet = [0] * 26
for i in range(len(s)):
    alphabet[ord(s[i]) - 97] += 1
print(*alphabet)