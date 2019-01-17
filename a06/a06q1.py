##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 06, Problem 1
##==============================================================================

## Part a
      
def calc_exp(b,n):
    exponent = 0
    multiple = 1
    while 1 <= n:
        exponent += b ** n
        multiple = multiple * (b + n)
        ans = exponent + multiple
        n = n - 1
    return ans


## part b

def list_stat(lst):
    stat = [0, 0, 0, 0, 0]
    for i in lst:
        if type(i) == int:
            stat[0] += 1
        elif type(i) == float:
            stat[1] += 1
        elif type(i) == bool:
            stat[2] += 1
        elif type(i) == str:
            stat[3] += 1
        else:
            stat[4] += 1
    return stat
