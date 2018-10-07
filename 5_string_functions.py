"""
    Strings Functions
"""

myStr = 'Hello World'

# To Capitale Case
print myStr.capitalize()

# To Swap Case
print myStr.swapcase()

# To Upper Case
print myStr.upper()

# To Lower Case
print myStr.lower()

# Get lenght
print len(myStr)

# Replace words
print myStr.replace('World', 'Everyone')

# Count words
print myStr.count('l')

# Find first word occurence positon
print myStr.find('l')
print myStr.find('m') # print -1, the m character is not exist in myStr string
print myStr.find('l', 4) # begain the search from the fourth position

# Index , Return an error if doesn't find anythings
print myStr.index('l')
# print mystr.index('p') # This line return an error

# Check if start with
print myStr.startswith('Hello')
print myStr.startswith('H')
print myStr.startswith('el')

# Check if end with
print myStr.endswith('World')
print myStr.endswith('!')
print myStr.endswith('d')

# Check if all chars is alphanumeric
print myStr.isalnum() # return False because myStr containes a spaces that isn't alphanumeric
print 'Mohamed26'.isalnum() # return True

# Check if all chars is alphabetic
print myStr.isalpha() # return False because myStr containes a spaces that isn't alphabetic
print 'Mohamed'.isalpha() # return True 

# Check if all chars is numeric
# print myStr.isnumeric() # return False 
# print '2018'.isnumeric() # return True 


# Split to list
print myStr.split()
print myStr.split('l') # split when 'l' exist in myStr

# Join list items to get a string
listOfWords = myStr.split() # split list
print " ".join(listOfWords) # join list items with space
print ", ".join(listOfWords) # join list items with ', '

"""
    ...
"""