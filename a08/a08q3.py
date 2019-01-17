##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 08, Problem 3
##==============================================================================

import check

class Line:
    '''Fields: slope(anyof Int Float "undefined"), intercept (anyof Int Float)
          '''  
    
    def __init__(self,slope,intercept):
        self.slope = slope
        self.intercept = intercept
        
        
    def __repr__(self):
        s1 = "Y = {0:.2f}X + {1:.2f}"
        s2 = "X = {0:.2f}"
        s3 = "Y = {0:.2f}"
        if self.slope=="undefined":
            return s2.format(self.intercept)
        elif self.slope==0:
            return s3.format(self.intercept)
        else:
            return s1.format(self.slope, self.intercept)
    
    def __eq__(self, other):
            return type(other) == type(self) and self.slope == other.slope and \
                   self.intercept == other.intercept    
        
    ## part(a)
    ## points_to_line(x1,y1,x2,y2) produces a Line that go through the two consumed 
    ##  distinct points which through 4 parameters (x1, y1, x2, y2)
    ## points_to_line: Num Num Num Num -> Line
    ## Examples:
    ## Line.points_to_line(-7,6,9,6) -> Line(0,6)
    ## Line.points_to_line(-7,6.1,9.45,6) -> Line(-0.006079, 6.0574468)
    
    def points_to_line(x1,y1,x2,y2):
        if x1 - x2 == 0:
            m = "undefined"
            b = x1
        else:
            m = (y1 - y2) / (x1 - x2)
            b = y1 - m * x1
        line = Line(m,b)
        return line
        
    
    ## part(b) 
    ## perpendicular_line(self,x,y) produces a Line which goes through the given 
    ##  point(x,y) and is perpendicular to the object(self)
    ## perpendicular_line: Line Num Num -> Line
    ## Examples:
    ## for L3 = Line("undefined", 0), L3.perpendicular_line(3,4) => Line(0,4) 
    ## for L4 = Line(1,0) L4.perpendicular_line(4,0) => Line(-1,4) 
    
    def perpendicular_line(self,x,y):
        if self.slope == "undefined":
            m = 0
            b = y
        elif self.slope == 0:
            m = "undefined"
            b = x
        else:
            m = - (1 / self.slope)
            b = y - m * x
        line = Line(m,b)
        return line
        
    
    ## part(c)
    ## parallel(self, other) produces True if the consumed Line and the object(self) are parallel, otherwise produces False.
    ## parellel: Line Line -> Bool
    ## requires: other is different from self
    ## Examples:
    ## for L1=Line(10,4), L2=Line(10, -5), L1.parallel(L2) => True
    ## for L9=Line(9,2), L10=Line(2,3), L9.parallel(L10) => False 
    
    def parallel(self, other):
        if self.slope == other.slope:
            return True
        else:
            return False
        
    
    ## part(c)
    ## intersect(self, other) produces a list of length two that represents a point([x_coordinate,y_coordinate]) the represents the intersection point between the consumed Line and the object self. if both consumed Lines are paralled, tne the function return False.
    ## intersect: Line Line -> (anyof False (listof Num))
    ## requires: other is different from self
    ## Examples:
    ## for L5=Line("undefined",10), L6=Line(0,5), L5.intersect(L6) => [10, 5]
    ## L1.intersect(L2) => False
    
    def intersect(self, other):
        if not (self.parallel(other)):
            if self.slope == "undefined":
                x = self.intercept
                y = other.slope * x + other.intercept
            elif other.slope == "undefined":
                x = other.intercept
                y = self.slope * x + self.intercept
            else:
                x = (other.intercept - self.intercept) / (self.slope - other.slope)
                y = self.slope *x + self.intercept
            return [x,y]
        else:
            return False
    
            
   
# end of Line class
## constants for tests
L1 = Line(10,4)
L2 = Line(10, -5) 
L3 = Line("undefined", 0)
L4 = Line(1,0) 
L5 = Line("undefined",10)
L6 = Line(0,5)
L7 = Line(0,-9) 
L8 = Line(2,4) 
L9 = Line(9,2)
L10 = Line(2,3)
L11 = Line("undefined",3)
L12 = Line(0,3)
## Testing points_to_line(x1,y1,x2,y2)
check.expect("Q3T1",Line.points_to_line(-7,6,9,6), Line(0,6))
check.within("Q3T2", Line.points_to_line(-7,6.1,9.45,6).slope, -0.0061, 0.0001)
check.within("Q3T2", Line.points_to_line(-7,6.1,9.45,6).intercept, 6.0574, 0.0001) 
check.expect("Q3T3",Line.points_to_line(-9,10,-9,3),Line("undefined",-9))

## Testing perpendicular_line(self,x,y)
check.expect("Q3T4", L3.perpendicular_line(3,4), Line(0,4))
check.expect("Q3T5", L4.perpendicular_line(4,0), Line(-1,4))
check.expect("Q3T6", L7.perpendicular_line(-34,13), Line("undefined",-34))
check.within("Q3T7", L8.perpendicular_line(3,5), Line(-0.5000,6.5000), 0.0001)

## Testing parallel(self, other)
check.expect("Q3T8", L1.parallel(L2), True)
check.expect("Q3T9", L9.parallel(L10), False)
check.expect("Q3T10", L3.parallel(L11), True)
check.expect("Q3T11", L3.parallel(L1), False)
check.expect("Q3T12", L7.parallel(L12), True)
check.expect("Q3T13", L7.parallel(L10), False)

## Testing intersect(self, other)
check.expect("Q3T14", L5.intersect(L6), [10,5])
check.expect("Q3T15", L1.intersect(L2), False)
check.expect("Q3T16", L5.intersect(L1), [10,104])
check.within("Q3T17", L6.intersect(L1), [0.1000,5.000], 0.0001)
check.expect("Q3T18", L1.intersect(L11), [3,34])
check.within("Q3T19", L8.intersect(L9), [0.2857,4.5714], 0.0001)