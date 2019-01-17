##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 07, Problem 2
##==============================================================================

import check
## ternary_search(nlsl, val) prints out the information about the steps performed 
##  at runtime when consumes a non empty list of interge nlst, and an integer val
## Effects: prints out the information about the steps performed at runtime
## ternary_search: (listof Int) Int -> None
## requires: nlst is non empty
## Examples:
## For L=[6,12,18,22], ternary_search(L, 18) produces None and print:
## Checking if 18 is equal to 6
## Checking if 18 is equal to 12
## Checking if 18 is equal to 18
## Search successful
## 18 is located at index 2
## A total of 3 comparisons were made
## For ternary_search([6,12,18,22,29,37,38,41,51,53,55,67,73,75,77,81,86,88,94], 27) produces None and print:
## Checking if 27 is equal to 38
## Checking if 27 is less than 38
## Checking if 27 is equal to 18
## Checking if 27 is less than 18
## Checking if 27 is equal to 29
## Checking if 27 is less than 29
## Checking if 27 is equal to 22
## Search not successful
## A total of 7 comparisons were made

equal_string = "Checking if {0} is equal to {1}"
less_than_string = "Checking if {0} is less than {1}"
success = "Search successful"
failure = "Search not successful"
location = "{0} is located at index {1}"
comparisons = "A total of {0} comparisons were made"

def linear_search(nlst,val):
    for i in nlst:
        n += 1
        print(equal_string.format(val,i))
        if i == val:
            print(success)
            print(location.format(val,nlst.index(i)))
            print(comparisons.format(n))
            return  
        
def ternary_search(nlst, val):
    if len(nlst) <= 4:
        return linear_search(nlst,val)
    else:
        while len(nlst) > 4:
            ind1 = len(nlst)//3
            if len(nlst) % 3 > 0:
                ind2 = ind1 * 2 + 1
            else:
                ind2 = ind1 * 2            
            print(equal_string.format(val,ind1))
            if nlst[ind1] == val:
                n += 1
                print(success)
                print(location.format(val,ind1))
                return
            elif val < nlst[ind1]:
                print(less_than_string.format(val,ind1))
                n += 1
                nlst = nlst[:ind1]
            elif val == nlst[ind2]:
                print(less_than_string.format(val,ind1))
                print(equal_string.format(val,ind2))
                n += 1
                print(success)                                
                print(location.format(val,ind2))
                return 
            elif val < nlst[ind2]:
                print(less_than_string.format(val,ind1))
                print(equal_string.format(val,ind2))
                print(less_than_string.format(val,ind2))
                n += 1 
                nlst = nlst[ind1+1:ind2]
            else:
                print(less_than_string.format(val,ind1))
                print(equal_string.format(val,ind2))
                print(less_than_string.format(val,ind2))
                n += 1 
                nlst = nlst[ind2+1:ind3]                
                
            
                           