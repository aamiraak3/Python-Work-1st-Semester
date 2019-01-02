## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(mark):

    marks = int(round(mark))
	
    if marks >= 90:
        return "A+"
		
    elif marks >= 86:
        return "A"
		
    elif marks >= 82:
        return "A-"
		
    elif marks >= 78:
        return "B+"
		
    elif marks >= 74:
        return "B"
		
    elif marks >= 70:
        return "B-"
		
    elif marks >= 66:
        return "C+"
		
    elif marks >= 62:
        return "C"
		
    elif marks >= 58:
        return "C-"
		
    elif marks >= 54:
        return "D+"
		
    elif marks >= 50:
        return "D"
		
    elif marks >=0:
        return "F"
		
    else:
        return None
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def cgpa(y):
    
    if y == 'A':
        return 4.00
    elif y == 'A-':
        return 3.67
    elif y == 'B+':
        return 3.33
    elif y == 'B':
        return 3.00
    elif y == 'B-':
        return 2.67
    elif y == 'C+':
        return 2.33
    elif y == 'C':
        return 2.00
    elif y == 'C-':
        return 1.67
    elif y == 'D+':
        return 1.33
    elif y == 'D':
        return 1.00
    elif y == 'F':
        return 0.00
    else:
        return None
    
def calculate_sgpa(sub1, sub2, sub3):
    
    total_marks = 0
	
    total_num_of_subs = 0
    
    if sub1 != 'nothing':
        total_marks = total_marks + cgpa(sub1)
        total_num_of_subs = total_num_of_subs + 1
		
    if sub2 != 'nothing':
        total_num_of_subs = total_num_of_subs + 1
        total_marks = total_marks + cgpa(sub2)
		
    if sub3 != 'nothing':
        total_num_of_subs = total_num_of_subs + 1
        total_marks = total_marks + cgpa(sub3)
        
    sgpa = total_marks / total_num_of_subs
    return sgpa
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
