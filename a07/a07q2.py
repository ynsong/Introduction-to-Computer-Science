##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 07, Problem 2
##==============================================================================

import check

## Constants for ternary_search
equal_string = "Checking if {0} is equal to {1}"
less_than_string = "Checking if {0} is less than {1}"
success = "Search successful"
failure = "Search not successful"
location = "{0} is located at index {1}"
comparisons = "A total of {0} comparisons were made"

## ternary_search(nlsl, val) prints out the information about the steps performed 
##  at runtime when consumes a non empty list of interge nlst, and an integer val
## Effects: prints out the information about the steps performed at runtime
## ternary_search: (listof Int) Int -> None
## requires: nlst is non empty
## Examples:
## For L=[6,12,18,22], ternary_search(L, 18) => None and print:
## Checking if 18 is equal to 6
## Checking if 18 is equal to 12
## Checking if 18 is equal to 18
## Search successful
## 18 is located at index 2
## A total of 3 comparisons were made
## For ternary_search([6,12,18,22,29,37,38,41,51,53,55,67,73,75,77,81,86,88,94], 27)\
##  => None and print:
## Checking if 27 is equal to 38
## Checking if 27 is less than 38
## Checking if 27 is equal to 18
## Checking if 27 is less than 18
## Checking if 27 is equal to 29
## Checking if 27 is less than 29
## Checking if 27 is equal to 22
## Search not successful
## A total of 7 comparisons were made

def ternary_search(nlst, val):
        n = 0
        L = nlst.copy()
        while len(nlst) > 4:
                ind1 = len(nlst)//3
                if len(nlst) % 3 > 0:
                        ind2 = ind1 * 2 + 1
                else:
                        ind2 = ind1 * 2            
                print(equal_string.format(val,nlst[ind1]))
                if nlst[ind1] == val:
                        n += 1
                        print(success)
                        print(location.format(val,L.index(val)))
                        print(comparisons.format(n))
                        return
                elif val < nlst[ind1]:
                        print(less_than_string.format(val,nlst[ind1]))
                        n += 2
                        nlst = nlst[:ind1]
                elif val == nlst[ind2]:
                        print(less_than_string.format(val,nlst[ind1]))
                        print(equal_string.format(val,nlst[ind2]))
                        n += 3
                        print(success)                                
                        print(location.format(val,L.index(val)))
                        print(comparisons.format(n))
                        return 
                elif val < nlst[ind2]:
                        print(less_than_string.format(val,nlst[ind1]))
                        print(equal_string.format(val,nlst[ind2]))
                        print(less_than_string.format(val,nlst[ind2]))
                        n += 4 
                        nlst = nlst[ind1+1:ind2]
                else:
                        print(less_than_string.format(val,nlst[ind1]))
                        print(equal_string.format(val,nlst[ind2]))
                        print(less_than_string.format(val,nlst[ind2]))
                        n += 5 
                        nlst = nlst[ind2+1:]
        else:
                for i in nlst:
                        n += 1
                        print(equal_string.format(val,i))
                        if i == val:
                                print(success)
                                print(location.format(val,L.index(val)))
                                print(comparisons.format(n))
                                return
                else:
                        print(failure)
                        print(comparisons.format(n))

## Constants for test:
M1 = [6,12,18,22,29,37,38,41,51,53,55,67,73,75,77,81,86,88,94]
M2 = [6,12,18,22,29,37,38,41,51,53,55,67,73,75,77,81,86,88,94,103]
M3 = [6,12,18,22,29,37,38,41,51,53,55,67,73,75,77,81,86,88,94,103,130]

## Testing fot ternary_search(nlst,val): 
check.set_screen("Checking if 27 is equal to 1\nSearch not successful\nA total of\
 1 comparisons were made")
check.expect("len is 1 and target not in lst", ternary_search([1], 27), None)
check.set_screen("Checking if 27 is equal to 27\nSearch successful\n27 is located\
at index 0\nA total of 1 comparisons were made")
check.expect("len is 1 and target in lst", ternary_search([27], 27), None)
check.set_screen("Checking if 18 is equal to 6\nChecking if 18 is equal to 12\n\
Checking if 18 is equal to 18\nSearch successful\n18 is located at index 2\n\
A total of 3 comparisons were made")
check.expect("len is 4 and target in lst", ternary_search([6,12,18,22],18), None)
check.set_screen("Checking if 19 is equal to 6, Checking if 19 is equal to 12\n\
Checking if 19 is equal to 18\nChecking if 19 is equal to 22\nSearch not successful\n\
A total of 4 comparisons were made")
check.expect("len is 4 and target not in lst", ternary_search([6,12,18,22],19), None)
check.set_screen("ternary_search(M1,12)")
check.expect("len is 19_1",ternary_search(M1,12), None)
check.set_screen("ternary_search(M1, 27)")
check.expect("len is 19_2", ternary_search(M1, 27), None)        
check.set_screen("ternary_search(M1,38)")
check.expect("len is 19_3",ternary_search(M1,38), None)
check.set_screen("ternary_search(M1,51)")
check.expect("len is 19_4",ternary_search(M1,51), None)
check.set_screen("ternary_search(M1,56)")
check.expect("len is 19_5",ternary_search(M1,56), None)
check.set_screen("ternary_search(M1,75)")
check.expect("len is 19_6",ternary_search(M1,75), None)
check.set_screen("ternary_search(M1,86)")
check.expect("len is 19_7",ternary_search(M1,86), None)
check.set_screen("ternary_search(M1,87)")
check.expect("len is 19_8",ternary_search(M1,87), None)
check.set_screen("ternary_search(M2,87)")
check.expect("len is 20",ternary_search(M2,87), None)
check.set_screen("ternary_search(M3,87)")
check.expect("len is 21",ternary_search(M3,87), None)



                          