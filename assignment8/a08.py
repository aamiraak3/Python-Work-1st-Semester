## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types(dic):        #defining new function

    lst = []               # here a made an empty list to which values will be added 

    for i in dic:          # using for loop
        lst.append(i)      # then i append values in the above list

    print lst
    print type(lst)

    return lst
#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types_counts(cont):    # defining another function
    
    r = {}                     # making empty dictionary
    
    for j in cont:             # using for loop

        for i in j:            # another nasted loop
            v = cont[j]    
            r [j] = len (v)

        print r
    print type(r)
    return r

#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###
def get_author_count(d, author):

    count = 0                               # empty counter 

    for i in d:                               # for loop
        for j in d[i]:                        # again nested for loop
            for x in j:                           #   for loop
                if x == 'author':               #using if condition
                    for b in j[x]:
                        if j[x] [b]==author:      # another if condition
                            count += 1           # addition in counter
                            print type(count)

    print count

    return count

print 'done'

#### End OF MARKER





if __name__ == '__main__':
    d = {
            "articles": [{
                "slug": "how-to-train-your-mule",
                "title": "How to train your mule",
                "description": "Ever wonder how?",
                "body": "It takes a Jacobian",
                "tagList": ["mules", "training"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 0,
                "author": {
                  "username": "jake",
                  "bio": "I work at statefarm",
                  "following": False
                }
            }, {
                "slug": "and another article",
                "body": "I'm getting bored",
                "tagList": ["bored", "article"],
                "createdAt": "2016-02-18T03:22:56.637Z",
                "updatedAt": "2016-02-18T03:48:35.824Z",
                "favoritesCount": 20,
                "author": {
                  "username": "cap",
                  "following": True
                }
            }],
            "tweets": [{
                "body": "See my article on training mules.",
                "author": {
                  "username": "jake"
                }
            }]
        }

    print get_types(d)
    print get_types_counts(d)
    print get_author_count(d, 'cap')

    print get_author_count(d, 'jake', ['articles', 'tweets'])
