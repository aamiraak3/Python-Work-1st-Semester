## IMPORTS GO HERE
from math import pi
## END OF IMPORTS 
	

#### YOUR CODE FOR get_area GOES HERE ####
def get_area(radius):
	area = pi * pow(radius,2)
	return area
#### End OF MARKER


#### YOUR CODE FOR output_parameter GOES HERE 
def output_parameter(radius):
	r = radius
	paremeter = 2* pi*radius
	print 'The parameter of the circle with radius',radius,'is', paremeter
#### End OF MARKER  




if __name__ == '__main__': 
    print get_area(2) 
    output_parameter(1.0) 

