def print_art(msg):
    f = open("letters.txt","r")
    data = f.readlines()
    f.close()
    lst_msg = list(msg)
    start = ord("A")
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    line5 = ''
    
    for i in lst_msg:
        if i.isalpha():
            letter = ord(i.upper())
            start_line = 6 * (letter - start)
            print(start_line)
            line1 += data[start_line]
            line2 += data[start_line + 1][:-1]
            line3 += data[start_line + 2][:-1]
            line4 += data[start_line + 3][:-1]
            line5 += data[start_line + 4][:-1]
        else:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            line4 += '    '
            line5 += '    '
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    