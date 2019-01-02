
## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x, guess = 0.0):
    if x < 0.00000:
        return None
    if good_enough(guess, x):
        return guess

    else:
        new_guess = improve_guess(guess, x)
        return sqrt(x, new_guess)

def good_enough(guess, x):
    if abs(float(guess * guess - x)) < 0.00001:
        return True
    else:
        return False
#### End OF MARKER

#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(guess, x):
    a = (abs(guess + x) / 2.00000)
    return a


#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(guess, x):
    g = guess * 1.00000
    n = x * 1.00000

    if guess < 1.00000:
        return g + 5.00000
    else:
        return average(g, n/g)

#### End OF MARKER




if __name__ == '__main__':
    print sqrt(36)
