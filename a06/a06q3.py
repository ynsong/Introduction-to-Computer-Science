##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 06, Problem 3
##==============================================================================

import check

## trending(slst): produces a list of the most frequently occurring strings in 
##  a non-empty list of string slst
## trending: (listof Str) -> (listof Str)
## requires: slst is non-empty
## Examples:
## trending(["cs116", "Ihatehomework", "StarWars", "StarWars","cs116",
##  "uWaterloo", "CS116"]) => ["cs116", "StarWars"]
## trending(["cs116", "Ihatehomework", "StarWars", "Starwars","cs116", 
##  "uWaterloo"]) => ["cs116"]

def trending(slst):
    max_lst = [slst[0]]
    max_occurence =slst.count(slst[0])
    for i in slst:
        if slst.count(i) > max_occurence:
            max_lst = [i]
        elif (slst.count(i) == max_occurence) and (i not in max_lst):
            max_lst.append(i)
    return max_lst

## Testing for trending(slst):
check.expect("one element", trending(["cs116"]), ["cs116"])
check.expect("one string", trending(["cs116", "Ihatehomework", "StarWars",\
                                     "Starwars","cs116", "uWaterloo"]), ["cs116"])
check.expect("one string1", trending(["a", "b", "c", "c", "a", "b", "c"]), ["c"])
check.expect("all string have same occurence", \
             trending(["a", "a", "b", "b", "c", "c", "a", "b", "c"]), ["a", "b", "c"])
check.expect("more than one string",\
             trending(["cs116", "Ihatehomework", "StarWars", "StarWars","cs116",\
                       "uWaterloo", "CS116"]), ["cs116", "StarWars"])


 