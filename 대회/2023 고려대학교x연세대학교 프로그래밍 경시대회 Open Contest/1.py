kor = ['K', 'O', 'R', 'E', 'A']
yon = ['Y', 'O', 'N', 'S', 'E', 'I']
s = input()
for i in range(len(s)):
    if s[i] == kor[0]:
        kor.pop(0)
    if s[i] == yon[0]:
        yon.pop(0)
    if len(kor) == 0:
        print("KOREA")
        break
    elif len(yon) == 0:
        print("YONSEI")
        break