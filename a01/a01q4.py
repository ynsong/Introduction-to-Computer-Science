##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 01, Problem 2
##==============================================================================

import check

## max3(a, b, c) produces the maximal value among the three consumed value a, b, c.
## max3: Int Int Int -> Int
## Examples: max3(1, 1, 1) => 1
##           max3(4, 14, -3) => 14

def max3(a, b, c):
    max2 = ((a + b) / 2) + (abs (a - ((a + b) / 2)))
    return ((c + max2) / 2) + (abs (c - ((c + max2) / 2)))

## Testing for max3:
check.expect("Test three values are same", max3(1, 1, 1), 1)
check.expect("Test three different values", max3(4, 14, -3), 14)
check.expect("Test two values are same", max3(2, 2, 5), 5)
check.expect("Test two values are same 2", max3(-15, -199, -15), -15)
