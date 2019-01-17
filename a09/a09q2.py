##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 09, Problem 2
##==============================================================================

import check

## print_art(msg, filename): writes the data to draw the image corresponding to 
##  a nonempty string msg, and basd on a required filename and returns None
## Effects: writes a file to draw the imge corresponding to msg 
## print_art: Str Str -> None
## requires: msg is nonempty and only contain at least one English letter and space
## Examples:
## print_art("Nice Work dear", "result.txt") =>

N = 5

def print_art(msg, filename):
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
            line1 += data[start_line][:-3] + ' '
            line2 += data[start_line + 1][:-3] + ' '
            line3 += data[start_line + 2][:-3] + ' '
            line4 += data[start_line + 3][:-3] + ' '
            line5 += data[start_line + 4][:-3] + ' '
        else:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            line4 += '    '
            line5 += '    '
    out = open(filename, "w")
    out.writelines([line1 + "\n",line2 + "\n",line3 + "\n",line4 + "\n",line5 + "\n"])
    out.close()


## Testing for print_art(msg, filename):
check.set_file_exact("result.txt","Q2T1.txt")
check.expect("Q2T1", print_art("Nice Work dear", "result.txt"), None)
## test "hello"
check.set_file_exact("hello.txt","Q2T2.txt")
check.expect("Q2T2", print_art("hello", "hello.txt"), None)
## test "I am a girl"     
check.set_file_exact("I am a girl.txt","Q2T3.txt")
check.expect("Q2T3", print_art("I am a girl", "I am a girl.txt"), None)    
            
            
            
    
   