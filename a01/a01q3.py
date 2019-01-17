##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 01, Problem 2
##==============================================================================

import check

## forever_15(n) produces (3n + 45) * 2 / 6 - n
## forever_15: Nat -> Int
## Examples: forever_15(20) => 15
##           forever_15(150) => 15

def forever_15(n):
    return (((((n * 3) + 45) * 2) / 6) - n)

## Testing for forever_15:
check.expect("Test 1", forever_15(20), 15)
check.expect("Test 2", forever_15(150), 15)
check.expect("Test 3", forever_15(2), 15)
check.expect("Test 4", forever_15(299), 15)


