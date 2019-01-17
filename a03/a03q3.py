##==============================================================================
##  Yining Song (20675284)
##  CS 116 Spring 2017
##  Assignment 03, Problem 3
##==============================================================================

import check


## is_password_uppercase(password) produces True if the comsumed password is 
##   contained at least one uppercase character, otherwise False.
## is_password_uppercase: Str -> Bool

def is_password_uppercase(password):
    n = len(password)
    if n == 0:
        return False
    if password[(n - 1)].isupper():
        return True
    else:
        return is_password_uppercase(password[:(n - 1)])


## is_password_lowercase(password) produces True if the comsumed password is 
##   contained at least one lowercase character, otherwise False.
## is_password_lowercase: Str -> Bool

def is_password_lowercase(password):
    n = len(password)
    if n == 0:
        return False
    if password[(n - 1)].islower():
        return True
    else:
        return is_password_lowercase(password[:(n - 1)])
                                              

## is_password_digit(password) produces True if the comsumed password is 
##   contained at least one digit character, otherwise False.
## is_password_digit: Str -> Bool

def is_password_digit(password):
    n = len(password)
    if n == 0:
        return False
    if password[(n - 1)].isdigit():
        return True
    else:
        return is_password_digit(password[:(n - 1)]) 
    

## count_special_chars(password) produces the number of characters in the string
##   password that are not alphabetic charaters and digits
## count_special_chars: Str -> Int

def count_special_chars(password):
    n = len(password)
    if n == 0:
        return 0
    if password[(n - 1)].isdigit() or password[(n - 1)].isupper() or\
       password[(n - 1)].islower():
        return count_special_chars(password[:(n - 1)])
    else:
        return 1 + count_special_chars(password[:(n - 1)])


## score(password) produces the score for the accpeted password as required
## score: Str -> Int

def score(password):
    score = 0
    if count_special_chars(password) > 0:
        score = (count_special_chars(password) - 1) * 10
    if len(password) < 5:
        score = score-10
    if len(password) > 8:
        score = score + 15
    return score
            
   
## password_check (password) produces False and prints formatted message if 
##   consumed string passowrd is rejected, otherwise returns a string 
##   formatted as "score:strength" 
## Effects: prints formatted message
## password_check: Str -> (anyof Str False)
## Examples: 
## password_check("Xy 37 1-0") => "35:medium"
## password_check("Password999?") => "15:weak"
## password_check("Yt3)(*&a%") => "55:strong"
## password_check("PaSsWoRd") => False, and prints
## The password ("PaSsWoRd") failed a basic test
## password_check("hello12") => False, and prints
## The password ("hello12") failed a basic test

def password_check(password):
    msg1 = 'The password ("{0}") failed a basic test'
    res1 = "strong"
    res2 = "medium"
    res3 = "weak"
    if is_password_uppercase(password) and is_password_lowercase(password)\
       and is_password_digit(password):
        if score(password) < 20:
            return str(score(password)) + ":" + res3
        if 20 <= score(password) <= 40:
            return str(score(password)) + ":" + res2
        else:
            return str(score(password)) + ":" + res1
    else:
        print(msg1.format(password)) 
        return False
    
## Testing for password_check(password):
check.expect("no special character and lens less than 5", password_check("Aa1"),"-10:weak") 
check.expect("no special character and lens more than 8", password_check("Aa10000000"),"15:weak") 
check.expect("no special character and lens is 5", password_check("Aa100"),"0:weak")
check.expect("no special character and lens is 6", password_check("Aa1000"),"0:weak") 
check.expect("no special character and lens is 8", password_check("Aa100000"),"0:weak") 
check.expect("1 special character and lens is 6", password_check("Aa1 00"),"0:weak")
check.expect("1 special character and lens less than 5", password_check("Password999?"),"15:weak")
check.expect("2 special characters and lens is 6", password_check("Aa1//0"),"10:weak") 
check.expect("3 special characters and lens more than 8", password_check("Xy 37 1-0"),"35:medium") 
check.expect("strong score", password_check("Yt3)(*&a%"), "55:strong")
check.expect("score is 20", password_check("Aa1///00"), "20:medium")
check.expect("score is 40", password_check("Aa1/////"), "40:medium")
check.set_screen('The password ("PaSsWoRd") failed a basic test')
check.expect("no digit", password_check("PaSsWoRd"), False)
check.set_screen('The password ("hello12") failed a basic test')
check.expect("no uppercase char", password_check("hello12"), False)
check.set_screen('The password ("HELLO12") failed a basic test')
check.expect("no lowercase char", password_check("HELLO12"), False)
check.set_screen('The password ("hello") failed a basic test')
check.expect("only lowercase chars", password_check("hello"), False)
check.set_screen('The password ("12") failed a basic test')
check.expect("only digits", password_check("12"), False)
check.set_screen('The password ("ABCDE") failed a basic test')
check.expect("only uppercase chars", password_check("ABCDE"), False)
check.set_screen('The password ("") failed a basic test')
check.expect("empty", password_check(""), False)
check.set_screen('The password ("@#$%^&") failed a basic test')
check.expect("only special chars", password_check(("@#$%^&")), False)




 










       
    
            
        