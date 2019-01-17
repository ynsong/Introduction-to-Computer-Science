##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 09, Problem 1
##==============================================================================

import check

## school_courses(data) reads data from a required file called data and outputs 
##  a dictionary as required.
## Effects: read data from a file and created a dict from the data
## school_courses: Str -> (dictof Str (listof Str))
## Examples:
## school_courses("S17.txt") => {'CS115': ['Alice Dean', 'Dave Brown', 'Mary Sue'],\
##  'MATH135': ['Alice Dean', 'Dave Brown'], 'CHEM100': ['Alice Dean', 'Dave Brown', 'Mary Sue'],\
##  'MATH200': ['Alice Dean', 'Mary Sue']}
## school_courses("Q1T2.txt") => {"CS115": ["Dave Brown"]}

def school_courses(data):
    f = open(data,"r")
    courses = {}
    student = f.readline().strip()
    line = f.readline()
    
    while line != "":
        if line == "\n":
            student = f.readline().strip()
        else:
            line = line.strip().upper()
            if line in courses:
                courses[line].append(student)
            else:
                courses[line] = [student]
        line = f.readline()
    
    f.close()
    
    for i in courses:
        list.sort(courses[i])
    return courses

## Testing for school_courses(data):
check.expect("Q1T1", school_courses("S17.txt"), \
             {'CS115': ['Alice Dean', 'Dave Brown', 'Mary Sue'],\
              'MATH135': ['Alice Dean', 'Dave Brown'], \
              'CHEM100': ['Alice Dean', 'Dave Brown', 'Mary Sue'], \
              'MATH200': ['Alice Dean', 'Mary Sue']})
## "Q1T2.txt": "Dave Brown\nCs115\nMath135\nChem100"
check.expect("Q1T2", school_courses("Q1T2.txt"),\
             {'CS115': ['Dave Brown'],\
              'MATH135': ['Dave Brown'], \
              'CHEM100': [ 'Dave Brown']})
## "Q1T3.txt": "Alice Dean\nCs115\n\nMarry Sue\ncs115\n\nLily\nCS115"
check.expect("Q1T3", school_courses("Q1T3.txt"),\
             {'CS115': ['Alice Dean', 'Lily', 'Marry Sue']})
               

