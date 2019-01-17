##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 02, Problem 4
##==============================================================================

import check
## power_of(x,n) produces the value of x**n
## power_of: Int Int -> Float
## Examples:
## power_of(-3,0) => 1
## power_of(3,2) => 9
## power_of(5,-1) => 0.2
## power_of(-3, -1) => -0.3333

def power_of(x,n):
    if n>=0:
        if n == 0:
            return 1
        else:
            return x*(power_of(x, n-1))
    elif n<0:
        return 1/(power_of(x,(abs(n))))

## Testing for power_of:
check.within("-3 0",power_of(-3,0),1,0.00001)
check.within("3 2",power_of(3,2),9,0.00001)
check.within("5 -1",power_of(5,-1),0.2,0.00001)
check.within("-3 -1",power_of(-3, -1),-0.33333,0.00001)
check.within("0 0",power_of(0,0),1,0.00001)
check.within("-5 -2",power_of(-5,-2),0.04,0.00001)
check.within("20 20",power_of(20,20),104857600000000000000000000,0.00001)


