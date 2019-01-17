##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 01, Problem 1
##==============================================================================

import math

def f1(x,y):
    return ((y * 3) ** 2) // x


def f2(a,b):
    return (a - b) ** (b % 10)


def f3(n):
    return (math.sqrt(2 * math.pi * n)) * ((n / math.e) ** n)
    