##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 06, Problem 2
##==============================================================================

## part a

def create_evens(target):
    evens = []
    b = 2
    while b <= (target) :
        evens.append(b)
        b = b + 2
    return evens
        
    
## part b

def build_special_list(n):
    lst = []
    for i in range(n):
        sub_lst = []
        for x in range(i + 1):
            sub_lst.append(x + 1)
        lst.append(sub_lst)
    return lst
            

## part c

def divisibles(n):
    lst = []
    for i in range(n-1):
        if n % (i+1) == 0:
            lst.append(i+1)
    return lst


## part d

def update_list(nlst, val, newval):
    times = 0
    for i in range(len(nlst)):
        if nlst[i] == val:
            nlst[i] = newval
            times += 1
    return times