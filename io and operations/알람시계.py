from datetime import *
temp1, temp2 = input().split()
time_1 = timedelta(hours= int(temp1), minutes = int(temp2))
time_2 = timedelta(minutes = 45)
if time_1 < time_2 :
    time_1 = time_1 + timedelta(hours=24)
alarm = time_1 - time_2
alarm2 = str(alarm).split(":")
print(int(alarm2[0]), int(alarm2[1]))
#문제번호 2884번