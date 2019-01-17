##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 02, Problem 3
##==============================================================================

import check
## Constants for direct_transportation
Yes = "Yes"
No = "No"


## direct_transportation(orig, dest) produces "Yes" if there is a transportation
##  from the site, orig, to the site, dest, and "No" otherwise based on the given table
## direct_transportation: Str Str -> (anyof "Yes" "No")
## requires: orig and dest is any of "A" "B" "C" "D" "E" "F" "G"
## Examples:
## direct_transportation("F","F") => "Yes"
## direct_transportation("D","E") => "Yes"
## direct_transportation("F","A") => "No"
 
def direct_transportation(orig, dest):
    if orig == "A":
        return Yes
    elif orig == "B":
        if dest == "B" or dest == "D" or dest == "F" or dest == "G":
            return Yes
        else:
            return No
    elif orig == "C":
        if dest == "C" or dest == "D" or dest == "G":
            return Yes
        else:
            return No            
    elif orig == "D":
        if dest == "E" or dest == "D" or dest == "G":
            return Yes
        else:
            return No            
    elif orig == "E":
        if dest == "E" or dest == "F" or dest == "G":
            return Yes
        else:
            return No      
    elif orig == "F": 
        if dest == "F" or dest == "G":
            return Yes
        else:
            return No   
    elif orig == "G": 
        if dest == "G":
            return Yes
        else:
            return No 

## Testing for direct_transportation:
check.expect("F F",direct_transportation("F","F"), "Yes")
check.expect("D E",direct_transportation("D","E"), "Yes")
check.expect("F A",direct_transportation("F","A"), "No")

check.expect("A A",direct_transportation("A","A"), "Yes")
check.expect("A B",direct_transportation("A","B"), "Yes")
check.expect("A C",direct_transportation("A","C"), "Yes")
check.expect("A D",direct_transportation("A","D"), "Yes")
check.expect("A E",direct_transportation("A","E"), "Yes")
check.expect("A F",direct_transportation("A","F"), "Yes")
check.expect("A G",direct_transportation("A","G"), "Yes")

check.expect("B A",direct_transportation("B","A"), "No")
check.expect("B B",direct_transportation("B","B"), "Yes")
check.expect("B C",direct_transportation("B","C"), "No")
check.expect("B D",direct_transportation("B","D"), "Yes")
check.expect("B E",direct_transportation("B","E"), "No")
check.expect("B F",direct_transportation("B","F"), "Yes")
check.expect("B G",direct_transportation("B","G"), "Yes")

check.expect("C A",direct_transportation("C","A"), "No")
check.expect("C B",direct_transportation("C","B"), "No")
check.expect("C C",direct_transportation("C","C"), "Yes")
check.expect("C D",direct_transportation("C","D"), "Yes")
check.expect("C E",direct_transportation("C","E"), "No")
check.expect("C F",direct_transportation("C","F"), "No")
check.expect("C G",direct_transportation("C","G"), "Yes")

check.expect("D A",direct_transportation("D","A"), "No")
check.expect("D B",direct_transportation("D","B"), "No")
check.expect("D C",direct_transportation("D","C"), "No")
check.expect("D D",direct_transportation("D","D"), "Yes")
check.expect("D F",direct_transportation("D","F"), "No")
check.expect("D G",direct_transportation("D","G"), "Yes")

check.expect("E A",direct_transportation("E","A"), "No")
check.expect("E B",direct_transportation("E","B"), "No")
check.expect("E C",direct_transportation("E","C"), "No")
check.expect("E D",direct_transportation("E","D"), "No")
check.expect("E E",direct_transportation("E","E"), "Yes")
check.expect("E F",direct_transportation("E","F"), "Yes")
check.expect("E G",direct_transportation("E","G"), "Yes")

check.expect("F B",direct_transportation("F","B"), "No")
check.expect("F C",direct_transportation("F","C"), "No")
check.expect("F D",direct_transportation("F","D"), "No")
check.expect("F E",direct_transportation("F","E"), "No")
check.expect("F G",direct_transportation("F","G"), "Yes")

check.expect("G A",direct_transportation("G","A"), "No")
check.expect("G B",direct_transportation("G","B"), "No")
check.expect("G C",direct_transportation("G","C"), "No")
check.expect("G D",direct_transportation("G","D"), "No")
check.expect("G E",direct_transportation("G","E"), "No")
check.expect("G F",direct_transportation("G","F"), "No")
check.expect("G G",direct_transportation("G","G"), "Yes")