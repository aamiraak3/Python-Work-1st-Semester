# This Program find max odd and even in two separate functions

def finding_max_even():
    y = 0
    for counter in range(3):                   # Range of numbers can be changed
        x = int(input("Enter a number: "))
        if (x%2 == 0 and x > y):
            y = x
    if (y == 1):
        print("Sorry! All are odd")    
    else:
        print("Largest Even number is :",y )
(finding_max_even())

def finding_max_odd():
    y = 0
    for counter in range(3):                   # Range of numbers can be changed
        x = int(input("Enter a number : "))
        if (x%2 == 1 and x > y):
            y = x
    if (y == 0):
        print("Sorry! All are even")
    else:
        print("Largest Odd number is : ",y)        
finding_max_odd()            