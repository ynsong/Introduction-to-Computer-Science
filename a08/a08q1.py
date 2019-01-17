##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 08, Problem 1
##==============================================================================

import check

## freq_table(nlst) produces a dictionary representing the numbers in a non-empty 
##  list of integers nlst and their frequencies, and print a basic average 
##  statement in the format required.
## Effect: prints a basic average statement
## freq_table: (listof Int) -> (dictof Int Int)
## requires: nlst in non-empty
## Examples:
## freq_table([1]) => {1:1} and print Average = (1*1)/(1)
## freq_table([1,2,3,4,5,6,4,87,98,88,98,98]) => \
## {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1, 87: 1, 98: 3, 88: 1} and print 
##  Average = (1*1+2*1+3*1+4*2+5*1+6*1+87*1+98*3+88*1)/(1+1+1+2+1+1+1+3+1)

def freq_table(nlst):
    d = {}
    statement = "Average = ({0})/({1})"
    total_sum = ""
    key_sum = ""
    for element in nlst:
        if element in d:
            d[element] = d[element] + 1
        else:
            d[element] = 1
    for key in d:
        total_sum += str(key) + "*" + str(d[key]) + "+"
        key_sum += str(key) + "+"
    print(statement.format(total_sum[:-1],key_sum[:-1]))
    return d

## Testing freq_table(nlst)
check.set_screen("Average = (1*1)/(1)")
check.expect("Q1t1", freq_table([1]), {1:1})
check.set_screen("Average = (1*1+2*1+3*1+4*2+5*1+6*1+87*1+88*1+98*3)/(1+2+3+4+5+6+87+88+98)")
check.expect("Q1T2", freq_table([1,2,3,4,5,6,4,87,98,88,98,98]),\
             {1: 1, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1, 87: 1, 98: 3, 88: 1})
check.set_screen("Average = (1*1+2*1+-7*1+0*1)/(1+2+-7+0)")
check.expect("Q1t1", freq_table([1,2,-7,0]), {1:1, 2:1, -7:1, 0:1})
check.set_screen("Average = (999*2+888*2)/(999+888)")
check.expect("Q1t1", freq_table([999,888,888,999]), {999:2, 888:2})
        
    