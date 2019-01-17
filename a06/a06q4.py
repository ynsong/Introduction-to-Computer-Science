##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 06, Problem 4
##==============================================================================

import check
## digit_sum(num) produces the digit sum of a natural number num as required
## digit_sum: Nat -> Nat
## Examples:
## digit_sum(8) => 8
## digit_sum(897) => 6

def digit_sum(num):
    total_sum = 0
    while 0 < num:
        total_sum += num % 10
        num = num // 10
    if total_sum > 9:
        return digit_sum(total_sum)
    return total_sum

## Testing fot digit_sum(num):
check.expect("one digit num", digit_sum(0), 0)
check.expect("one digit num2", digit_sum(8), 8)
check.expect("digit sum less than 10", digit_sum(602), 8)
check.expect("digit sum greater than 9", digit_sum(897), 6)
check.expect("large number", digit_sum(77789), 2)



    
        
        
        
    
        