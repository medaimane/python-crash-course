"""
    Conditionals Statments
"""
age = 26
color = 'green'
people = ['John', 'Aimane', 'Mohamed', 'Haitam']

# Basic if
if age > 25:
    print 'You have more than 25 years old'

# if/elif/else
if age > 25:
    print 'You have more than 25 years old'
elif age == 25:
    print 'You have 25 years old'
else:
    print 'You have less than 25 years old'

# Nested if
if age > 25:
    if color == 'green':
        print 'Hy!'
    else:
        print 'Hello'
else:
    print 'No'

# Logical Operators
if age == 25 and color == 'green':
    print 'hy!'
elif age > 25 or color == 'blue':
    print 'hello!'
else:
    print 'hello'

# Advanced usecase
if 'Mohamed' in people:
    print True
else:
    print False