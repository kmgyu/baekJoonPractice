#5597번
sub_list = []
for i in range(28):
    sub_list.append(int(input()))
sub_set = set(sub_list)
comp = set(range(1,31))
sub_list = list(comp - sub_set)
if sub_list[0] > sub_list[1]:
    sub_list[0], sub_list[1] = sub_list[1], sub_list[0]
for i in sub_list : print(i)

