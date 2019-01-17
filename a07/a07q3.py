##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 07, Problem 3
##==============================================================================

import check

## merge(La,Lb,Lc) merge La and Lb in ascending order and put back into L, L is 
##  combined length of L1 and L2
## Effects: mutating La and Lb and put them back into L
## merge: (listof Int) (listof Int) (listof Int) -> None
## requires: L1 and L2 in increasing order

def merge(La,Lb,Lc):
    posa, posb, posc = 0, 0, 0
    while (posa < len(La)) and (posb < len(Lb)):
        if La[posa] < Lb[posb]:
            Lc[posc] = La[posa]
            posa +=1
        else:
            Lc[posc] = Lb[posb]
            posb +=1
        posc += 1
    while (posa < len(La)):
        Lc[posc] = La[posa]
        posa, posc = posa+1, posc+1
    while (posb < len(Lb)):
        Lc[posc] = Lb[posb]
        posb, poc = posb+1, posc+1


## mergesort3(L) mutates a list of integer L by sorting it in ascending order.
## Effect: mutating L by sorting it in ascending order
## mergesort3: (listof Int) -> None
## requires: No duplicate values in L
## Examples:
## For lst = [1,4,3,2], calling mergesort3(lst) => None, and mutate lst as [1,2,3,4]
## For lst = [5,8,2,4,3,1,9,6], calling mergesort3(lst) => None, and mutate lst as [1,2,3,4,5,6,8,9]

def mergesort3(L):
    if len(L) <= 4:
        n = len(L)
        positions = list(range(n-1))
        for i in positions:
            min_pos = i
            for j in range(i,n):
                if L[j] < L[min_pos]:
                    min_pos = j
            temp = L[i]
            L[i] = L[min_pos]
            L[min_pos] = temp
    else:
        ind1 = len(L)//3
        if len(L) % 3 > 0:
            ind2 = ind1 * 2 + 1
        else:
            ind2 = ind1 * 2 
        L1 = L[:ind1]
        L2 = L[ind1:ind2]
        L3 = L[ind2:]
        M = L[:ind2]
        mergesort3(L1)
        mergesort3(L2)
        mergesort3(L3)
        merge(L1,L2,M)
        merge(M,L3,L)
        
## Testing for mergesort3(L):
lst1 = [1,4,3,2]
check.expect("len equals 4", mergesort3(lst1), None)
check.expect("test lst1", lst1, [1,2,3,4])
lst2 = [1,4,3]
check.expect("len less than 4", mergesort3(lst2), None)
check.expect("test lst2", lst2, [1,3,4])
lst3 = []
check.expect("empty lst", mergesort3(lst3), None)
check.expect("test lst3", lst3, [])
lst4 = [5,8,2,4,3,1,9,6]
check.expect("len is 8", mergesort3(lst4), None)
check.expect("test lst4", lst4, [1,2,3,4,5,6,8,9])
lst5 = [234,535,32,435,321,33,67,78,-304]
check.expect("len is 9", mergesort3(lst5), None)
check.expect("test lst5", lst5, [-304,32,33,67,78,234,321,435,535])
lst6 = [-19,234,535,32,435,321,33,67,78,-304]
check.expect("len is 10", mergesort3(lst6), None)
check.expect("test lst6", lst6, [-304,-19,32,33,67,78,234,321,435,535])