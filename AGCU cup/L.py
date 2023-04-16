#010 2
#110 3
#001 4
#101 5
#011 6
#111 7
a = input()
bit = ''
for i in a:
    if i == 'O':
        bit += '0'
    elif i == 'X':
        bit += '1'
bit = int('0b'+''.join(reversed(bit)),2)
print( (((0b1 << len(a))-1) - bit) % (10**9 + 7))
# OXXOXOXOXOOXXXXOXOOOXOOXXOOOXOXOXOXO
# X00X0X0X0XX0000X0XXX0XX00XXX0X0X0X0X = 524287