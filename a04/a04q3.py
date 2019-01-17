##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 04, Problem 3
##==============================================================================

import check

## A keycode is a list of length 2, [d, n] where
##   d is an int from 0 - 9 representing a digit on a phone keypad and
##   n is an int[>0], representing the number of times the key has
##        been pressed. The value of n will be less than or equal to
##        the number of symbols associated with d on a phone.

def keycode_message(k):
    if k[0] == 0:
        return " "
    elif k[0] == 1:
        if k[1] == 1:
            return "."
        elif k[1] == 2:
            return ','
        elif k[1]== 3:
            return '?'
    elif k[0] == 2:
        elif k
    
            
        


## compose_msg(keypresses) produces a string that represents a text message base 
##  on the consumed keypresses which is a list of keycode
## compose_msg: (listof keycode) -> Str
## Examples:
## compose_msg([[6, 3], [0, 1], [5, 2]]) => string "o k"  
def compose_msg(keypresses):