##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 05, Problem 1
##==============================================================================

import check
import math

## calc_exp(b,n) produces the sum of (b+b^2+b^3+...+b^n) and (b+1)(b+2)...(b+n) by 
##  consuming two positive natural number b and n
## cal_exp: Nat Nat -> Nat
## requires: b > 0
##           n > 0
## Examples: 
## calc_exp(10,1) => 21
## calc_exp(3,4) => 960

def calc_exp(b,n):
    ## cala_power_acc(so_far,a,b,n) adds b^a, b^(a+1),..., b^n to the end of so_far
    ## cala_power_acc: Nat Nat Nat Nat -> Nat
    ## requires: b > 0
    ##           n > 0
    def calc_power_acc(so_far,a,b,n):
        if a > n:
            return so_far
        else:
            so_far = so_far + math.pow(b,a) 
            return calc_power_acc(so_far,a + 1,b,n)
    ## cala_plus_acc(so_far,a,b,n) multiplies b+a, b+(a+1),..., b+n to the end of so_far
    ## cala_plus_acc: Nat Nat Nat Nat -> Nat
    ## requires: b > 0
    ##           n > 0    
    def calc_plus_acc(so_far,a,b,n):
        if a > n:
            return so_far
        else:
            so_far = so_far * (b + a)
            return calc_plus_acc(so_far,a + 1,b,n)    
    ## Body of calc_exp:
    return calc_power_acc(0,1,b,n) + calc_plus_acc(1,1,b,n)

## Testing for calc_exp(b,n):
check.expect("n = 1", calc_exp(10,1), 21)
check.expect("b = 1", calc_exp(1,5), 725)
check.expect("n = 1, b = 1", calc_exp(1,1), 3)
check.expect("n = 4, b = 3", calc_exp(3,4), 960)

