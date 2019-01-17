##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 05, Problem 4
##==============================================================================

import check

## replace_str(base,target,rep) produces a string that uses rep to replace target 
##   in the base and if the target string is not found in the base string or if 
##   the target and rep are the same string then produces the base
## replace_str: Str Str Str -> Str
## requires: base, target, rep are non-empty
## Examples:
## replace_str("This is a book","a","the") => 'This is the book'
## replace_str("This is my book","a","the") => 'This is my book'
## replace_str("I like this book","I","I") =>  'I like this book'
## replace_str("my brother reads books and sometimes he reads magazines",\
##   "reads", "likes") => 'my brother likes books and sometime he likes magazines'
## replace_str("Apple is a fruit", "f" , "t") => 'Apple is a truit'
## replace_str("aaaaa","aa","x") => 'xxa'
    
def replace_str(base, target, rep):
    ## base_lst(lst,rep) produces a string by adding the string rep between each
    ##   element in a list of string lst
    ## (listof Str) Str -> Str
    ## requires: lst and rep are non-empty
    def base_lst(lst,rep):
        if len(lst) <= 1:
            return lst[0] 
        else:
            return lst[0] + rep + base_lst(lst[1:],rep) 
    ## Body of replace_str:
    return base_lst(base.split(target),rep)

## Testing replace_str(base,target,rep):
check.expect("target is not found in the base",replace_str("This is my book","a","the")\
             ,'This is my book')            
check.expect("target and rep are the same",replace_str("I like this book","I","I")\
             ,'I like this book') 
check.expect("one target in the base",replace_str("This is a book","a","the")\
             ,'This is the book') 
check.expect("two target in the base",\
             replace_str("my brother reads books and sometimes he reads magazines","reads","likes") 
             ,'my brother likes books and sometimes he likes magazines') 
check.expect("target inside a word",replace_str("Apple is a fruit","f" ,"t")\
             ,'Apple is a truit') 
check.expect("target is at the begining",replace_str("Apple is a fruit","Apple","Peach")\
             ,'Peach is a fruit') 
check.expect("target are adjacent",replace_str("aaaaa","aa","x")\
             ,'xxa') 
check.expect("target is at the end",replace_str("Apple is a fruit","fruit" ,"milk")\
             ,'Apple is a milk')
        
        
