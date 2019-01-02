## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###


# here i defined another function as 'grade marks which takes one argunment' 
#its function is to assign grade to marks.
def grade_marks (marks):
    if marks == 'A+':
        return 4.00
    elif marks == 'A':
        return 4.00
    elif marks == 'A-':
        return 3.67
    elif marks == 'B+':
        return 3.33
    elif marks == 'B':
        return 3.00
    elif marks == 'B-':
        return 2.67
    elif marks == 'C+':
        return 2.33
    elif marks == 'C':
        return 2.00
    elif marks == 'C-':
        return 1.67
    elif marks == 'D+':
        return 1.33
    elif marks == 'D':
        return 1.00
    elif marks == 'F':
        return 0.00
    else:
        return None
def calculate_sgpa(x):       #     here defining the function for calculate sgpa
    
    total_marks = 0
    
    total_subjects = len (x)
    
    for i in x:
        if i == None or grade_marks (i) == None or type (i) == int :
            return None
        total_marks = grade_marks (i) + total_marks
    
    return total_marks / total_subjects

#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted (y, z):   # to find weightage i made another function 
    
    credit_hrs = 0.0     # which take credit hours
    
    divider = 0.0          # and the number through it is going to be divided
    
    score = 0.0           # and the score of subs
    
    if len (y) != len (z):    # as length of y is not equal to length z so it will return None
        return None
    
    else:                      #otherwise it will give us the following equation
        for a in (y):
            score = grade_marks(a)
            return type(score)
            for b in (z):
                credit_hrs = credit_hrs + b
                divider = divider + score + b
                return type(divider), type(credit_hrs)
                return type(divider / credit_hrs)
        return divider / credit_hrs

#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(['A+'])
    temp = calculate_sgpa_weighted(['A+'], [4])
    print temp
