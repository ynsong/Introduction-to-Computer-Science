##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 03, Problem 2
##==============================================================================

import check

## generate_username() produces a string, username, made up from the first name, 
##   last name and birth year promoted as required
## Effect: Prints prompts to the user and reads in your first name, your last 
##  last name, and your birth year
## generate_username: None -> Str
## Examples:
## If the user enters "Mike", "Brown", "1989" when generate_username() is called,
##   mrown891 is produced
## If the user enters "Young", "Hu", "1991" when generate_username() is called,
##   "yhu991" is produced

def generate_username():
    inp1 = input('Enter your first name:')
    inp2 = input('Enter your last name:')
    inp3 = input('Enter your birth year:')
    return inp1[0].lower() + inp2[(len(inp2) - 4):].lower() + (inp3[::-1])[1:]

## Testing for generate_username():
check.set_input(["Mike", "Brown", "1989"])
check.expect("Mike Brown 1989", generate_username(), "mrown891")
check.set_input(["Young", "Hu", "1991"])
check.expect("Young Hu 1991", generate_username(), "yhu991")
check.set_input(["Lilly", "Annabell", "2003"])
check.expect("Lilly Annabell 2003", generate_username(), "lbell002")