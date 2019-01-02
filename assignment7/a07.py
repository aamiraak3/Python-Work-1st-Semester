## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(x):
# here i will assigin variable A to zero
    A = 0
# And then i wrote the condition to handle the case on None     
    if x == None:
    	print type(x)
        return None
#the assignment marks is reffered to zero    
    for Q in x:
        ass_marks = 0
# AND THEN I ASSIGNED IT TO A NEW VARIABLE        
        P = Q
#uSING FOR LOOP        
        for i in P:
            if i == None: # AS IF ARGUNMENTS OF IS = nONE SO MARKS WILL BE ADDED TO 0
                ass_marks += 0
                S = list(P) # and then will be packed as list
                S.remove(i) # so we will remove if from the list by 'remove' cmd 
                P = tuple(S) # and then will assign it as tuple
                
            if type(i) == int or type(i) == float: # converting string into int or float type for addition                                                                  
                ass_marks += i
                S = list(P)     # assign as list
                S.remove(i)  #  removing argunments
                P = tuple(S)
                
        S = list(P)

        S.append(ass_marks)

        P = tuple(S)

        x[A] = P

        A += 1

    print type(x)
    return (x)  
    


#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(topper):  # FINDING MARKS OF TOPPER STUDENTS
	
    G = topper[1]
    
    a_list = []
    
    if (len(topper[0]) == 3):
        for i in range (0, len(topper)):
            if topper[i][2] == G[2]:
            	G = topper[i]
            	T = list(G)
            	T.remove(T[2])
            	N = tuple(T)
            	a_list.append(N)
            	print type(a_list)

        print type(a_list)

    	return a_list


    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]
    
    
  

    
    K = find_cumulative_marks(topper)
    
    M = K[1]
    
    for i in range(0, len(K)):
        if K[i][2] >  M[2]:
            M = K[i]

    B = list(M)

    B.remove(B[2])

    M = tuple(B)

    return M


#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
