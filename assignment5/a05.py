## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def output_prime_factors(opf):           # defining function 

    if type(opf) == float:               # converting into integer and then rounding off
        opf = int(round(opf))
        
    for i in range(1, opf + 1):          # now using for loop 
        ok = opf % i
        
        if ok == 0:                      # now using if condition
            of = is_prime(i)
            
            if of == True:               # again if conditon
                print i
                
        else:                            # using else
            i = i + 1



def is_prime(num):                       # defining is_prime

	if num == 2:                         # using if condition
		return True

	if num > 1:                          # again using if condition
		for og in range(2, num):

			if (num % og) == 0:          # again if condition
				return False
				break

		else:                            # again else
			return True 


#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(nth):                 # defining function

    if nth == 1:                        # if loop
        return 2

    count = 1                             

    num = 3

    while(count <= nth):                # using while loop

        if is_prime(num):
            count += 1

            if count == nth:
                return num

        num += 2


#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
