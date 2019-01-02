 ## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(n):

    if type(n) == float:
        n = int (n)


    if n < 2:
        return False

    else:
    	for j in range(2, n):
    	   if n % j == 0:
                return False

           else:
                return True


    
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(k):

	for n in range (1, k + 1):
			if k % n == 0:
				print (n)

#### End OF MARKER


#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def prime_for_largest(l):

    if l == 0 or l == 2 or l == 3 or l == 5 or l == 7:
        return l

    if l % l == 0 and l % 2 != 0 and l % 3 != 0 and l % 5 != 0:
        return l

    else:
        return False


def get_largest_prime(m):

    if m < 2:
        return None 

    if type(m) == float:
        m = int(m)


    prime = []

    if prime_for_largest(m):
        prime.append(m)

    for i in range(1, m):

        if prime_for_largest(1):
            prime.append(1)

    return max(prime)

    
#### End OF MARKER



if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
