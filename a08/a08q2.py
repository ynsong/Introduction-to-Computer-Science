##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 08, Problem 2
##==============================================================================

import check

## constants for exmaples and tests
term1={"Eng100":[1,3,4,5,7,8,9,10,11], "CS116" :[1,3,4,5,6,7,8,10], \
       "Math135":[1,3,4,5,7,8,9,10,11]}
term2={"CS116":[11,12,13,14,15], "Math135":[11,12,34,56,44], "Drama":[11,12,34,56,44,111]}
term3 = {"Math138":[11,12,13,14,15], "CS115":[1,3,4,5,6,7,8,10]}
term4 = {"Eng100":[1,3,4,35,7,8,99,10,11], "CS116" :[1,3,4,5,6,78,8,10], \
         "Math135":[1,3,4,5,7,8,9,10,11,104]}

##Part a)
## most_popular_courses(term) produces a list of the most popular courses when
##  consumes a dictionary, term which stores the courese offered and the id of enrolled students.
## most_popular_courses: (dictof Str (listof Nat) -> (listof Str)
## requires: student id is a list of non-empty positive Nat
## Examples:
## most_popular_courses(term1) => ['Eng100', 'Math135']
## most_popular_courses(term2) => ['Drama']

def most_popular_courses(term):
    courses_lst = []
    max_student = 0
    for key in term:
        if len(term[key]) > max_student:
            max_student = len(term[key])
            courses_lst = [str(key)]
        elif len(term[key]) == max_student:
            courses_lst.append(str(key))
    return courses_lst

## Testing most_popular_courses(term)
check.expect("empty",most_popular_courses({}), [])
check.expect("one course",most_popular_courses({"CS116":[1,34,44,3]}), ["CS116"])
check.expect("two most popular courses",most_popular_courses(term1), ["Eng100","Math135"])
check.expect("one most popular course",most_popular_courses(term2), ["Drama"])
   
    
##Part b)
## common_courses(t1,t2) produces a list of all courses that offered in both 
## consumed terms t1 and t2.
## common_courses:(dictof Str (listof Nat) -> (listof Str)
## requires: student id is a list of non-empty positive Nat
## Examples:
## common_courses(term1,term2) => ['CS116', 'Math135']
## common_courses(term1,{}) => []

def common_courses(t1, t2):
    common = []
    for key in t1:
        if key in t2:
            common.append(key)
    return common

## Testing common_courses(t1,t2)
check.expect("empty", common_courses({},{}), [])
check.expect("t1 is empty", common_courses({},term1), [])
check.expect("t2 is empty", common_courses(term2,{}), [])
check.expect("have common courses", common_courses(term1,term2), ['CS116', 'Math135'])
check.expect("no common courses", common_courses(term1,term3), [])
          

##Part c)
## offered_once(t1,t2) produces a list of all courses that offered once in
## consumed terms t1 and t2.
## offered_once:(dictof Str (listof Nat) -> (listof Str)
## requires: student id is a list of non-empty positive Nat
## Examples:
## offered_once(term1,term2) => ['Eng100', 'Drama']
## offered_once(term1,{}) => ['Eng100', 'CS116', Math135]

def offered_once(t1, t2):
    once = []
    for key in t1:
        if not(key in t2):
            once.append(key)
    for key in t2:
        if not(key in t1):
            once.append(key)            
    return once

## Testing offered_once(t1,t2)
check.expect("empty", offered_once({},{}), [])
check.expect("t1 is empty", offered_once({},term1), ['Math135', 'CS116', 'Eng100'])
check.expect("t2 is empty", offered_once(term2,{}), ['CS116', 'Math135', 'Drama'])
check.expect("have offered_once courses", offered_once(term1,term2), ['Eng100', 'Drama'])
check.expect("no offered_once courses", offered_once(term1,term4), [])


##Part d)
## enroll_student(term, course, studid) produces False and prints a message as 
##  required if the students is already enrolled in the course or the course if not 
##  offered, otherwise mutates term by removeing studid in course when consume 
##  term, a course code course and a student id studid.
## Effects: mutates term by adding the studid in the course as required
## enroll_student: (dictof Str (listof Nat) Str Nat -> (anyof False or None)
## requires: value of term is a list of non-empty positive Nat
##           studid is positive
## Examples:
## for enroll_student(term1, "CS135", 300) => False and print: The course CS135 
##  is not offered in the provided term.
## for enroll_student(term1, "CS116", 5) => False and print: The student 5 is 
##  already enrolled in course CS116.
## for enroll_student(term1, "Math135", 300) => None and term1 is mutated to: 
## {'Eng100': [1, 3, 4, 5, 7, 8, 9, 10, 11], 'CS116': [1, 3, 4, 5, 6, 7, 8, 10],\ 
## 'Math135': [1, 3, 4, 5, 7, 8, 9, 10, 11, 300]}

def enroll_student(term, course, studid):
    enrolled = "The student {0} is already enrolled in course {1}."
    not_offered = "The course {0} is not offered in the provided term."
    if not (course in term):
        print(not_offered.format(course))        
        return False
    if studid in term[course]:
        print(enrolled.format(studid,course))
        return False
    else:
        term[course].append(studid)

## Testing for enroll_student(term,course,studid)
check.set_screen("The course CS116 is not offered in the provided term.")     
check.expect("empty term", enroll_student({},"CS116",300), False) 
check.set_screen("The course  is not offered in the provided term.")     
check.expect("empty course", enroll_student(term1,"",300), False)
check.set_screen("The course CS135 is not offered in the provided term.")     
check.expect("not offered", enroll_student(term1,"CS135",300), False)
check.set_screen("The student 5 is already enrolled in course CS116.")     
check.expect("already enrolled", enroll_student(term1,"CS116",5), False)     
check.expect("add studid", enroll_student(term1,"Math135",300), None)        
check.expect("test term1", term1, {'Eng100': [1, 3, 4, 5, 7, 8, 9, 10, 11], \
                                   'CS116': [1, 3, 4, 5, 6, 7, 8, 10], \
                                   'Math135': [1, 3, 4, 5, 7, 8, 9, 10, 11, 300]})

        
    
##Part e)
## drop_student(term, course, studid) produces False and prints a message as 
##  required if the students is not enrolled in the course or the course if not 
##  offered, otherwise mutates term by removeing studid in course when consume 
##  term, a course code course and a student id studid.
## Effects: mutates term by removing the studid in the course as required
## drop_student: (dictof Str (listof Nat) Str Nat -> (anyof False or None)
## requires: value of term is a list of non-empty positive Nat
##           studid is positive
## Examples:
## for drop_student(term1, "Eng100", 244)=> False and print: The student 244 is 
##  not enrolled in course Eng100.
## for drop_student(term1, "Eng200", 4) => False and print: The course Eng200 is 
##  not offered in the provided term.
## for drop_student(term1, "Eng100", 4) => None and term1 is mutated to: 
## {'Eng100': [1, 3, 5, 7, 8, 9, 10, 11], 'CS116': [1, 3, 4, 5, 6, 7, 8, 10], \
##  'Math135': [1, 3, 4, 5, 7, 8, 9, 10, 11]}

def drop_student(term, course, studid):
    not_enrolled = "The student {0} is not enrolled in course {1}."
    not_offered = "The course {0} is not offered in the provided term."
    if not (course in term):
        print(not_offered.format(course))        
        return False
    if not(studid in term[course]):
        print(not_enrolled.format(studid,course))
        return False
    else:
        lst = term[course]
        lst.pop(lst.index(studid))

## Testing drop_student(term,course,studid)
check.set_screen("The course CS116 is not offered in the provided term.")     
check.expect("empty term", drop_student({},"CS116",300), False) 
check.set_screen("The course  is not offered in the provided term.")     
check.expect("empty course", drop_student(term1,"",300), False)
check.set_screen("The course Eng200 is not offered in the provided term.")     
check.expect("not offered", drop_student(term1,"Eng200",4), False)
check.set_screen("The student 244 is not enrolled in course Eng100.")     
check.expect("already enrolled", drop_student(term1,"Eng100",244), False)
term1 = {"Eng100":[1,3,4,5,7,8,9,10,11], "CS116" :[1,3,4,5,6,7,8,10], \
       "Math135":[1,3,4,5,7,8,9,10,11]}
check.expect("remove studid", drop_student(term1,"Eng100", 4), None)        
check.expect("test term1", term1, {'Eng100': [1, 3, 5, 7, 8, 9, 10, 11], \
                                   'CS116': [1, 3, 4, 5, 6, 7, 8, 10], \
                                   'Math135': [1, 3, 4, 5, 7, 8, 9, 10, 11]})