##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 07, Problem 4
##==============================================================================

import check

## max_times(L) produces a list of length two, where the first element is the 
## maximal value in L and the second element is the number of times the maximal 
## value appears in L and L is a non empty list of a non empty list of integers
## max_time: (listof (listof Int)) -> (listof Int)
## requires: L is non empty
## Exmaples:
## max_times([[1,2,2,2,3],[2,2,1],[3,2,3,3]]) => [3,4]
## max_times([[-1]]) => [-1,1]

def max_times(L):
    max_val = L[0][0]
    times = 0
    for i in L:
        for j in i:
            if j > max_val:
                max_val = j
                times = 1
            elif j == max_val:
                times += 1
    max_lst = [max_val,times]
    return max_lst

## Testing for max_time(L):
check.expect("one element1",max_times([[-1]]), [-1,1])
check.expect("one element2",max_times([[-1,4,5,6]]), [6,1])
check.expect("one element3",max_times([[-1,-1,-1,-1]]), [-1,4])
check.expect("one maximal val", max_times([[-9,0,-22,33],[32,100,33,22]]), [100,1])
check.expect("more than one maximal vals1", max_times([[-9,0,-22,33],[32,100,33,22], [100]]), [100,2])
check.expect("more than one maximal vals2", max_times([[1,2,2,2,3],[2,2,1],[3,2,3,3]]), [3,4])
   