##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 05, Problem 2
##==============================================================================

import check

## list_stat(lst) produces a list containing exactly 5 natural numbers which calculates 
##   the number of different types of the elements in the consumed list lst in the order 
##   of integers, floats, booleans, strings and all of the other types
##  
## list_stat: (listof Any) -> (list of Nat)
## Examples:
## list_stat([3, "wow", -3.967, True, True, False, "nice"]) => [1, 1, 3, 2, 0]
## list_stat(["good", [3,4], [10]]) => [0, 0, 0, 1, 2]
## list_stat([]) => [0, 0, 0, 0, 0]

def list_stat(lst):
    ## list_stat_acc(lst,origin) produces a new list containing exactly 5 natural numbers  
    ##   by adding the number of different types of the elements in the consumed list lst 
    ##   and the each corrsponding number in the list origin
    ## list_stat_acc: (listof Any) (listof Nat) -> (listof Nat)
    def list_stat_acc(lst,origin):
        if lst == []:
            return origin
        elif type(lst[0]) == int:
            origin[0] = origin[0] + 1
            return list_stat_acc(lst[1:],origin)
        elif type(lst[0]) == float:
            origin[1] = origin[1] + 1
            return list_stat_acc(lst[1:],origin)
        elif type(lst[0]) == bool:
            origin[2] = origin[2] + 1
            return list_stat_acc(lst[1:],origin)
        elif type(lst[0]) == str:
            origin[3] = origin[3] + 1 
            return list_stat_acc(lst[1:],origin)
        else:
            origin[4] = origin[4] + 1
            return list_stat_acc(lst[1:],origin)
    ## Body of list_stat:
    return list_stat_acc(lst, [0, 0, 0, 0, 0])

## Testing for list_stat(lst):
check.expect("empty lst", list_stat([]), [0, 0, 0, 0, 0])
check.expect("lst only has ints", list_stat([1, 3, 43]), [3, 0, 0, 0, 0])
check.expect("lst only has floats", list_stat([1.324, 42.32]), [0, 2, 0, 0, 0])
check.expect("lst only has bools", list_stat([True, True, False]), [0, 0, 3, 0, 0])
check.expect("lst only has strs", list_stat(['1', 'as', 'sc']), [0, 0, 0, 3, 0])
check.expect("lst only has other types", list_stat([[12], ['as']]), [0, 0, 0, 0, 2])
check.expect("lst1", list_stat([3, "wow", -3.967, True, True, False, "nice"]), [1, 1, 3, 2, 0])
check.expect("lst2", list_stat(["good", [3,4], [10]]), [0, 0, 0, 1, 2])

        