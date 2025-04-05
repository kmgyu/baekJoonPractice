

input = open(0).readlines
doc=input()



one = ''
lines = []

one_line = ''
for line in doc:
    line = line.strip()
    line = line.split()
    
    for txt in line:
        if txt == '<br>':
            one_line += '\n'
            lines.append(one_line)
            one_line = ''
        elif txt == '<hr>':
            if one_line: one_line += '\n'
            one_line += '-' * 80 + '\n'
            lines.append(one_line)
            one_line = ''
        else:
            if len(one_line) + len(txt) + 1 > 80:
                lines.append(one_line+'\n')
                one_line = ''
            if one_line: one_line += ' '
            one_line += txt
            
if one_line:
    lines.append(one_line)
    one_line = ''


print(*lines, sep='')
