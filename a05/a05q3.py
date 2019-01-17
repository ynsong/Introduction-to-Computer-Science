##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 05, Problem 3
##==============================================================================

import check

## movesteps(n,source,target,helper) prints the required steps for first moving 
##   n-1 disks from the rod source to the rod helper, then moving the nth dist
##   from source to target, finally moving n-1 disks from helper to the target
## Effects: prints the steps for moving n disks as required
## movesteps: Nat Str Str Str -> None
## requires: n > 0

def movesteps(n,source,target,helper):
    if n > 0:
        movesteps(n - 1,source,helper,target)
        print('moving ' + str(n) + ' from ' + source + ' to ' + target)
        movesteps(n - 1,helper,target,source)   


## show(n) prints the steps required to finish the Towed of Hanoi game with n disks successfully
## Effect: prints the steps required to finish the Towed of Hanoi game with n disks successfully 
## show: Nat -> None
## requires: n > 0
## Examples:
## show(3) prints 
## moving 1 from source to target
## moving 2 from source to helper
## moving 1 from target to helper
## moving 3 from source to target
## moving 1 from helper to source
## moving 2 from helper to target
## moving 1 from source to target

def show(n):
    movesteps(n,"source","target","helper")
    
## Testing for show(n):
check.set_screen("show 1")
check.expect("show 1", show(1), None)
check.set_screen("show 2")
check.expect("show 2", show(2), None)
check.set_screen("show 3")
check.expect("show 3", show(3), None)
check.set_screen("show 4")
check.expect("show 4", show(4), None)