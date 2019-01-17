##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 01, Problem 2
##==============================================================================

import math 
import check

## normal_distribution(x, mean, std_dev) produces the corresponding value of 
##   normal distribution with x, mean, and standard deviation std_dev.
## normal_distribution: Float Float Float -> Float
## requires: x, mean, std_dev > 0
## Examples: normal_distribution(3, 5, 2) => 0.120

def normal_distribution(x, mean, std_dev):
    a = 1 / (std_dev * (math.sqrt (2 * math.pi)))
    b = 1 / (math.e ** (((x - mean) ** 2) / (2 * ((std_dev) ** 2))))
    return a * b

## Testing normal_distribution:
check.within("Test 1", normal_distribution(3, 5, 2), 0.120, 0.001)
check.within("Test 2", normal_distribution(1, 1, 1), 0.398, 0.001)

