##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 03, Problem 4
##==============================================================================

import check

## draw_diamond_helper1(rows, n) prints diamond of "$" which starts from the
##  the n rows and end with the rows row
## draw_diamond_helper1: Nat Nat -> None

def draw_diamond_helper1(rows,n):
    if n <= rows:
        the_longest_length = rows * 2 - 1
        number_of_space = ((the_longest_length - (2 * n - 1)) // 2)
        print(' ' * number_of_space  + '$' * (2 * n - 1) )
        draw_diamond_helper1(rows, n+1) 


## draw_diamond_helper2(rows, n) prints diamond of "$" which starts from the
##  the the rows row and end with n rows
## draw_diamond_helper2: Nat Nat -> None

def draw_diamond_helper2(rows,n):
    if n < rows:
        the_longest_length = rows * 2 - 1
        number_of_space = ((the_longest_length - (2 * (rows - n) - 1) )// 2)
        print(' ' * number_of_space + '$' * (2 * (rows - n) - 1))
        draw_diamond_helper2(rows, n+1)     
        
        
## draw_diamond(rows) conusumes a Int rows and print a diamond of "$" with the 
##   height of  2 * rows - 1
## Effects: print a diamond of "$" with the height of  2 * rows - 1
## draw_diamond: Nat -> None
## Examples:
## draw_diamond(0) => None
## draw_diamond(1) => print
## $
## draw_diamond(5) => print
##     $
##    $$$
##   $$$$$
##  $$$$$$$
## $$$$$$$$$$
##  $$$$$$$
##   $$$$$
##    $$$
##     $

def draw_diamond(rows):
    draw_diamond_helper1(rows,1)
    draw_diamond_helper2(rows,1)
    
## Tesrs for draw_diamond(rows):
check.set_screen("draw_diamond0")
check.expect("draw_diamond0", draw_diamond(0),None)
check.set_screen("draw_diamond1")
check.expect("draw_diamond1", draw_diamond(1),None)
check.set_screen("draw_diamond2")
check.expect("draw_diamond2", draw_diamond(2),None)
check.set_screen("draw_diamond5")
check.expect("draw_diamond5", draw_diamond(5),None)
check.set_screen("draw_diamond8")
check.expect("draw_diamond8", draw_diamond(8),None)
        
        