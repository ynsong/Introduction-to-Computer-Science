##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 07, Problem 1
##==============================================================================

# Question 1. 
#
# Determine the worst-case runtime of the following functions. 
# The answer will be stated in terms of the size of the problem.
#
# Note. In all cases, choose the 'tightest' bound.
#
# Choose 
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

# (a)
# Let n = len(L)
def fn_a(L):
    L1 = list(map(lambda x: x%2, L))
    L2 = list(filter(lambda y: y<5, L1))
    L3 = list(map(lambda z:5-z, L2))
    return len(L3)

# (b)
# Let n = len(s)
def fn_b(s):
    if len(s)==0:
        return ""
    else:
        return fn_b(s[1:])+fn_b(s[2:])

# (c)
# Let n = len(L)
def fn_c(L):
    def helper_c(r):
        a = []
        for k in range(len(L)):
            a.append(r)
        return a
    return list(map(helper_c, L))

# (d)
# Let n = len(L)
def fn_d(L, x):
    for i in range(len(L)):
        j=i
        while j<len(L):
            if L[i]+L[j]==x:
                return i+j
            j=j+1
    return -1

# (e)
# Let n = len(L)
def fn_e(L):
    ans = 0
    while L!=[]:
        ans=ans+L[0]
        L=L[1:]
    return ans>100
	
# (f)
# n is a natural number.
def fn_f(n):
    def helper_f(x):
        while x>1:
            x=x//2
    for k in range(n):
        helper_f(k)

# Place one of A,B,C,D,E or F inside the string quotes;
#e.g., if you think fn_a has a running time of O(2**n),
#then change a_answer = "" to a_answer = "F".
#
# Choose:
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

a_answer = "C"
b_answer = "F"
c_answer = "E"
d_answer = "E"
e_answer = "C"
f_answer = "D"