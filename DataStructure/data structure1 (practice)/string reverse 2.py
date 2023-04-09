#17413번 단어 뒤집기2
s = input()
li = list()
start_tag = 0
end_tag = 0
for i in range(0, len(s)):
    if s[i] == "<": # >나올때까지 리스트에 추가
        start_tag = i
    elif s[i] == ">":
        if end_tag == start_tag:
            pass
        else:
            li.append(s[end_tag:start_tag])
        li.append(s[start_tag:i+1])
        end_tag = i+1
    elif i == len(s)-1:
        li.append(s[end_tag:])
for i in range(len(li)):
    if li[i][0] != "<":
        temp = li[i].split()
        ans = ''
        for j in temp:
            ans += ''.join(reversed(j))+" "
        li[i] = ans.rstrip()
print(*li, sep="")

    #마지막에 +" " 해서 split하기 쉽게 만들기

#< 또는 > 찾으면 문자열 찢어서 " " 넣기
#이러면 문자열 새로생성해야함. 메모리+
# <이랑 > 찾는 시간복잡도 n

# case 1
# s = input()
# li = list()
# for i in range(0, len(s)):
#     if s[i] == "<": # >나올때까지 리스트에 추가
#         if s[i-1] == " ":
#             continue
#         s = s[:i] + " " + s[i:]
#     elif s[i] == ">":
#         s = s[:i+1] + " " + s[i+1:]
# li = list(s.split())