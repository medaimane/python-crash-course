# Variables and Data Types

# variable
greeting = 'Hello World!'
# reassigning value
# greeting = 2018

# Data Types
myStr = 'Mohamed Aimane'
myInt = 26
myFloat = 3000.5
myList = [myStr, myInt, myFloat]
myDict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'list': myList
    }

# logs
print greeting

print myDict['a']

print type(myDict), myDict
print type(myList), myList
print type(myFloat), myFloat
print type(myInt), myInt
print type(myStr), myStr

print greeting + ' from ' + myStr